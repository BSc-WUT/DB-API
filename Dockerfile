FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENV DATABASE_URL ${DATABASE_URL}

COPY src /app/src

COPY ./create_config.sh /app/create_config.sh

EXPOSE ${API_PORT}

CMD ["bash", "-c", "./create_config.sh && uvicorn src.main:app --host 0.0.0.0 --port ${API_PORT} --reload"]