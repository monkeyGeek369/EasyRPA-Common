from enum import Enum

class EasyRpaExceptionCodeEnum(Enum):
    '''数据异常(1-100)'''
    DATA_NULL = ('DataNull', 1, '数据为空')
    DATA_TYPE_ERROR = ('DataTypeError', 2, '数据类型错误')
    DATA_NOT_FOUND = ('DataNotFound', 3, '数据未找到')
    DATA_FORMAT_ERROR = ('DataFormatError', 4, '数据格式错误')
    DATA_VALUE_ERROR = ('DataValueError', 5, '数据值错误')
    DATA_NOT_MATCH = ('DataNotMatch', 6, '数据不匹配')