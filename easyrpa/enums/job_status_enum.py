from enum import Enum

class JobStatusEnum(Enum):
    DISPATCHING = ('Dispatching', 1, '调度中')
    DISPATCH_SUCCESS = ('DispatchSuccess', 2, '调度成功')
    DISPATCH_FAIL = ('DispatchFail', 3, '调度失败')