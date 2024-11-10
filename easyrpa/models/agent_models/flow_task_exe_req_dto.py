from dataclasses import dataclass

@dataclass
class FlowTaskExeReqDTO:
    task_id:int
    site_id:int
    flow_id:int
    flow_code:str
    flow_name:str
    flow_rpa_type:int
    flow_exe_env:str
    flow_standard_message:str
    flow_exe_script:str
    sub_source:int