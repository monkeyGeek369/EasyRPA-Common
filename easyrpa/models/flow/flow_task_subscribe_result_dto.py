from dataclasses import dataclass

@dataclass
class FlowTaskSubscribeResultDTO:
    task_id:int
    status:bool
    error_msg:str