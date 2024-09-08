from enum import Enum

class FlowTaskStatusEnum(Enum):
    WAIT_EXE = ('WaitExe', 1, '待执行')
    EXECUTION = ('Execution', 2, '执行中')
    SUCCESS = ('Success', 3, '成功')
    FAIL = ('Fail', 3, '失败')