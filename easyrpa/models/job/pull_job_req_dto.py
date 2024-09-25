from dataclasses import dataclass

@dataclass
class PullJobReqDTO:
    website:str
    channel_name:str
    channel_id:str
    video_tab:str
    list_start_index:int
    list_stop_index:int