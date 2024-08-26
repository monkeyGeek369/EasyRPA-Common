from enum import Enum

class EasyRpaExceptionCodeEnum(Enum):
    '''数据异常（1-100）'''
    DATA_NULL = ('DataNull', 1, '数据为空')
    DATA_TYPE_ERROR = ('DataTypeError', 2, '数据类型错误')

    def __init__(self, name, code, description):
        self.name = name
        self.code = code
        self.description = description