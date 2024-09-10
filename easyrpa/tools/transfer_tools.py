from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
from easyrpa.tools.str_tools import str_to_dict_first_level

def any_to_str_dict_first_level(param:any) -> dict:
    """将任何类型的对象转换为dict，只针对第一层级value值转换为str类型

    Args:
        param (any): 请求参数

    Raises:
        EasyRpaException: 异常信息

    Returns:
        dict: 结果字典
    """
    if not param:
        return None
    
    if isinstance(param, dict):
        # 将value全部转换为str类型
        return dict_to_str_dict_first_level(param)
    elif isinstance(param, list):
        raise EasyRpaException("param is list type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    elif isinstance(param, str):
        # 将str转换为dict类型
        dict_param = str_to_dict_first_level(param)
        
        return dict_param
    elif isinstance(param, object):
        # 将object转换为json字符串
        json_str = param.to_json()

        # 将json字符串转换为dict
        dict_param = str_to_dict_first_level(json_str)
        return dict_param
    else:
        # 不支持的数据类型
        raise EasyRpaException("param is not dict/str type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    

def dict_to_str_dict_first_level(param:dict) -> dict:
    """dict_to_str_dict_first_level convert dict to dict that value is str for fist level

    Args:
        param (dict): dict

    Returns:
        dict: dict that value is str
    """
    if not param:
        return None
    for key, value in param.items():
        param[key] = str(value)
    return param