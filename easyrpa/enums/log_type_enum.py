from enum import Enum

class LogTypeEnum(Enum):
    TXT = ('Txt', 1, '文字')
    SCREENSHOTS = ('Screenshots', 2, '截图')
    TASK_RESULT = ('TaskResult', 3, '任务结果')
    TASK_RESULT_NOTIFY = ('TaskResultNotify', 4, '任务结果通知')