from dataclasses import dataclass

@dataclass
class FlowTaskSubscribeDTO:
    flow_id:int
    flow_configuration_id:int
    biz_no:str
    sub_source:int
    request_standard_message:str
    flow_code:str