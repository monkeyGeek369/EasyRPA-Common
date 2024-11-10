from typing import List
from dataclasses import dataclass

@dataclass
class FlowTaskExeResDTO:
        task_id:int
        site_id:int
        flow_id:int
        flow_code:str
        flow_name:str
        flow_rpa_type:int
        flow_exe_env:str
        sub_source:int
        status:bool
        error_msg:str
        print_str:List[str]
        result:str
        code:str