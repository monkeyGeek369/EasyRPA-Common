from enum import Enum

class EasyRpaExceptionCodeEnum(Enum):
    '''数据异常(1-100)'''
    DATA_NULL = ('DataNull', 1, '数据为空')
    DATA_TYPE_ERROR = ('DataTypeError', 2, '数据类型错误')
    DATA_NOT_FOUND = ('DataNotFound', 3, '数据未找到')
    DATA_FORMAT_ERROR = ('DataFormatError', 4, '数据格式错误')
    DATA_VALUE_ERROR = ('DataValueError', 5, '数据值错误')
    DATA_NOT_MATCH = ('DataNotMatch', 6, '数据不匹配')

    '''系统异常(101-200)'''
    SYSTEM_ERROR = ('SystemError', 101, '系统异常')
    SYSTEM_BUSY = ('SystemBusy', 102, '系统繁忙')
    SYSTEM_TIMEOUT = ('SystemTimeout', 103, '系统超时')
    SYSTEM_NOT_FOUND = ('SystemNotFound', 104, '系统未找到')
    SYSTEM_NOT_CONFIG = ('SystemNotConfig', 105, '系统未配置')
    
    '''执行异常(201-300)'''
    EXECUTE_ERROR = ('ExecuteError', 201, '执行异常')