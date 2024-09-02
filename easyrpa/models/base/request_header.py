from dataclasses import dataclass
from datetime import datetime

@dataclass
class RequestHeader:
    user_id:int
    trace_id:str
    req_time:datetime