from dataclasses import dataclass
from easyrpa.models.base.request_header import RequestHeader


@dataclass
class RequestBaseModel:
    header:RequestHeader
    model:any