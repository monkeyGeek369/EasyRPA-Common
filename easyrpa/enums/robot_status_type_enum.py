from enum import Enum

class RobotStatusTypeEnum(Enum):
    CLOSED = ('closed', 1, '已关机')
    LEISURE = ('leisure', 2, '空闲')
    RUNNING = ('running', 3, '执行中')
    
    def get_by_id(id):
        for item in RobotStatusTypeEnum:
            if item.value[1] == id:
                return item