from dataclasses import dataclass

@dataclass
class ResponseBaseModel:
    status:bool
    code:int
    message:str
    data:any