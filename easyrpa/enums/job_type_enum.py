from enum import Enum

class JobTypeEnum(Enum):
    DATA_PULL = ('DataPull', 1, '数据爬取')
    DATA_PUSH = ('DataPush', 2, '数据推送')