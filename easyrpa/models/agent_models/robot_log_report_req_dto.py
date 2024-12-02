from dataclasses import dataclass

@dataclass
class RobotLogReportReqDTO:
    robot_code:str
    task_id:int
    log_type:int
    message:str
    