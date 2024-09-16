from dataclasses import dataclass
from easyrpa.models.base.request_header import RequestHeader


@dataclass
class ScriptExeParamModel:
    header: RequestHeader
    source: int
    standard: str
    flow_config:str