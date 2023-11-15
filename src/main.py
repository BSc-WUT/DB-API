from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os
import csv
import io

from .models import NetworkFlowMapping, NetworkFlow


def get_env_vars() -> dict:
    load_dotenv()
    return {
        "DB_HOST": os.getenv("DATABASE_HOST"),
        "DB_PORT": os.getenv("DATABASE_PORT"),
        "DB_USER": os.getenv("DATABASE_USER"),
        "DB_PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "API_PORT": os.getenv("API_PORT"),
    }


app = FastAPI()
ENV_VARS = get_env_vars()
NETWORK_FLOW_INDEX_NAME = "network_flows"

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_es() -> Elasticsearch:
    url: str = f"http://{ENV_VARS['DB_USER']}:{ENV_VARS['DB_PASSWORD']}@{ENV_VARS['DB_HOST']}:{ENV_VARS['DB_PORT']}"
    es: Elasticsearch = Elasticsearch(url)
    return es


es = get_es()


def network_flow_index_exists() -> None:
    if not es.indices.exists(index=NETWORK_FLOW_INDEX_NAME):
        raise HTTPException(
            status_code=404,
            detail=f"Index: {NETWORK_FLOW_INDEX_NAME} does exists in ElasticSearch database.",
        )


""" INDEXES """


@app.post("/indexes/create/{index_name}")  # ✅
def create_index(
    index_name: str, network_flow_mapping: NetworkFlowMapping
) -> JSONResponse:
    return es.indices.create(index=index_name, body=network_flow_mapping.dict())


@app.get("/indexes/{index_name}")  # ✅
def index_exists(index_name: str) -> JSONResponse:
    return es.indices.get(index=index_name)


""" NETWORK FLOWS """


@app.get("/network_flows/{flow_id}")  # ✅
def get_network_flow(flow_id: str) -> JSONResponse:
    network_flow_index_exists()
    try:
        results: dict = es.get(index=NETWORK_FLOW_INDEX_NAME, id=flow_id)
        results: dict = results.get("_source")
    except Exception as e:
        results: dict = {"error": str(e)}
    return results


@app.get("/network_flows")  # ✅
def get_all_network_flows() -> JSONResponse:
    network_flow_index_exists()
    query: dict = {"query": {"match_all": {}}}
    results: dict = es.search(
        index=NETWORK_FLOW_INDEX_NAME, doc_type="_doc", body=query
    )
    return results


@app.post("/network_flows")  # ✅
async def add_network_flow(network_flow: NetworkFlow) -> JSONResponse:
    network_flow_index_exists()
    return es.index(
        index=NETWORK_FLOW_INDEX_NAME, doc_type="_doc", body=network_flow.dict()
    )


@app.post("/network_flows/bulk_upload")  # ✅
async def bulk_network_flow_upload(bulk_file: UploadFile) -> JSONResponse:
    network_flow_index_exists()
    contents: dict = bulk_file.file.read()
    buffer: io.StringIO = io.StringIO(contents.decode("utf-8"))
    csvReader: csv.DictReader = csv.DictReader(buffer)
    docs: list = list(csvReader)
    print(docs)
    helpers.bulk(es, docs, index=NETWORK_FLOW_INDEX_NAME, doc_type="_doc")
    buffer.close()
    bulk_file.file.close()

    query: dict = {"query": {"match_all": {}}}
    results: dict = es.search(
        index=NETWORK_FLOW_INDEX_NAME, doc_type="_doc", body=query
    )
    return results
