from dataclasses import dataclass

@dataclass
class HeartbeatCheckReqDTO:
    robot_code:str
    robot_ip:str
    port:int
    task_id:int