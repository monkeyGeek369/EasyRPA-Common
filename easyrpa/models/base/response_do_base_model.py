from dataclasses import dataclass
from datetime import date

@dataclass
class ResponseDoBaseModel:
    created_id:int
    created_time:date
    modify_id:int
    modify_time:date
    trace_id:str
    is_active:bool