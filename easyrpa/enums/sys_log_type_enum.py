from enum import Enum

class SysLogTypeEnum(Enum):
    INFO = ('info', 1, '信息')
    WARN = ('warn', 2, '告警')
    DEBUG = ('debug', 3, '异常')
    BIZ = ('biz', 4, '业务')