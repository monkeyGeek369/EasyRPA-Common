from dataclasses import dataclass
from datetime import datetime

@dataclass
class FlowTaskExeResultNotifyDTO:
    site_id:int
    flow_id:int
    flow_task_id:int
    flow_config_id:int
    biz_no:str
    sub_source:int
    status:int
    result_code:int
    result_message:str
    result_data:str
    screenshot_base64:str
    created_id:int
    created_time:datetime