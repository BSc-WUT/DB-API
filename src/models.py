from pydantic import BaseModel, create_model
from typing import Dict


class Property(BaseModel):
    type: str


class NetworkFlowPropsObj(BaseModel):
    __root__: Dict[str, Property]


class NetworkFlowProperties(BaseModel):
    properties: NetworkFlowPropsObj


class NetworkFlowMapping(BaseModel):
    mappings: NetworkFlowProperties


NETWORK_FLOW_KEYS: list = [
    "Dst Port",
    "Protocol",
    "Timestamp",
    "Flow Duration",
    "Tot Fwd Pkts",
    "Tot Bwd Pkts",
    "TotLen Fwd Pkts",
    "TotLen Bwd Pkts",
    "Fwd Pkt Len Max",
    "Fwd Pkt Len Min",
    "Fwd Pkt Len Mean",
    "Fwd Pkt Len Std",
    "Bwd Pkt Len Max",
    "Bwd Pkt Len Min",
    "Bwd Pkt Len Mean",
    "Bwd Pkt Len Std",
    "Flow Byts/s",
    "Flow Pkts/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow IAT Max",
    "Flow IAT Min",
    "Fwd IAT Tot",
    "Fwd IAT Mean",
    "Fwd IAT Std",
    "Fwd IAT Max",
    "Fwd IAT Min",
    "Bwd IAT Tot",
    "Bwd IAT Mean",
    "Bwd IAT Std",
    "Bwd IAT Max",
    "Bwd IAT Min",
    "Fwd PSH Flags",
    "Bwd PSH Flags",
    "Fwd URG Flags",
    "Bwd URG Flags",
    "Fwd Header Len",
    "Bwd Header Len",
    "Fwd Pkts/s",
    "Bwd Pkts/s",
    "Pkt Len Min",
    "Pkt Len Max",
    "Pkt Len Mean",
    "Pkt Len Std",
    "Pkt Len Var",
    "FIN Flag Cnt",
    "SYN Flag Cnt",
    "RST Flag Cnt",
    "PSH Flag Cnt",
    "ACK Flag Cnt",
    "URG Flag Cnt",
    "CWE Flag Count",
    "ECE Flag Cnt",
    "Down/Up Ratio",
    "Pkt Size Avg",
    "Fwd Seg Size Avg",
    "Bwd Seg Size Avg",
    "Fwd Byts/b Avg",
    "Fwd Pkts/b Avg",
    "Fwd Blk Rate Avg",
    "Bwd Byts/b Avg",
    "Bwd Pkts/b Avg",
    "Bwd Blk Rate Avg",
    "Subflow Fwd Pkts",
    "Subflow Fwd Byts",
    "Subflow Bwd Pkts",
    "Subflow Bwd Byts",
    "Init Fwd Win Byts",
    "Init Bwd Win Byts",
    "Fwd Act Data Pkts",
    "Fwd Seg Size Min",
    "Active Mean",
    "Active Std",
    "Active Max",
    "Active Min",
    "Idle Mean",
    "Idle Std",
    "Idle Max",
    "Idle Min",
    "Label",
    "Flow ID",
    "Src IP",
    "Src Port",
    "Dst IP",
]


class NetworkFlow(BaseModel):
    label: str
    src_ip: str
    dst_ip: str
    src_port: str
    dst_port: str
    protocol: str
    timestamp: str
    flow_duration: str
    flow_byts_s: str
    flow_pkts_s: str
    fwd_pkts_s: str
    bwd_pkts_s: str
    tot_fwd_pkts: str
    tot_bwd_pkts: str
    totlen_fwd_pkts: str
    totlen_bwd_pkts: str
    fwd_pkt_len_max: str
    fwd_pkt_len_min: str
    fwd_pkt_len_mean: str
    fwd_pkt_len_std: str
    bwd_pkt_len_max: str
    bwd_pkt_len_min: str
    bwd_pkt_len_mean: str
    bwd_pkt_len_std: str
    pkt_len_max: str
    pkt_len_min: str
    pkt_len_mean: str
    pkt_len_std: str
    pkt_len_var: str
    fwd_header_len: str
    bwd_header_len: str
    fwd_seg_size_min: str
    fwd_act_data_pkts: str
    flow_iat_mean: str
    flow_iat_max: str
    flow_iat_min: str
    flow_iat_std: str
    fwd_iat_tot: str
    fwd_iat_max: str
    fwd_iat_min: str
    fwd_iat_mean: str
    fwd_iat_std: str
    bwd_iat_tot: str
    bwd_iat_max: str
    bwd_iat_min: str
    bwd_iat_mean: str
    bwd_iat_std: str
    fwd_psh_flags: str
    bwd_psh_flags: str
    fwd_urg_flags: str
    bwd_urg_flags: str
    fin_flag_cnt: str
    syn_flag_cnt: str
    rst_flag_cnt: str
    psh_flag_cnt: str
    ack_flag_cnt: str
    urg_flag_cnt: str
    ece_flag_cnt: str
    down_up_ratio: str
    pkt_size_avg: str
    init_fwd_win_byts: str
    init_bwd_win_byts: str
    active_max: str
    active_min: str
    active_mean: str
    active_std: str
    idle_max: str
    idle_min: str
    idle_mean: str
    idle_std: str
    fwd_byts_b_avg: str
    fwd_pkts_b_avg: str
    bwd_byts_b_avg: str
    bwd_pkts_b_avg: str
    fwd_blk_rate_avg: str
    bwd_blk_rate_avg: str
    fwd_seg_size_avg: str
    bwd_seg_size_avg: str
    cwe_flag_count: str
    subflow_fwd_pkts: str
    subflow_bwd_pkts: str
    subflow_fwd_byts: str
    subflow_bwd_byts: str
