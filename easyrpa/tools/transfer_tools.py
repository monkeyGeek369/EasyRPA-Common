from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
from easyrpa.tools.str_tools import str_to_str_dict

def any_to_str_dict(param:any) -> dict:
    if not param:
        return None
    
    if isinstance(param, dict):
        # 将value全部转换为str类型
        for key, value in param.items():
            param[key] = str(value)
        return param
    elif isinstance(param, list):
        raise EasyRpaException("param is list type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    elif isinstance(param, str):
        # 将str转换为dict类型
        dict_param = str_to_str_dict(param)
        
        return dict_param
    elif isinstance(param, object):
        # 将object转换为json字符串
        json_str = param.to_json()

        # 将json字符串转换为dict
        dict_param = str_to_str_dict(json_str)
        return dict_param
    else:
        # 不支持的数据类型
        raise EasyRpaException("param is not dict/str type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    

def dict_to_str_dict(param:dict) -> dict:
    """dict_to_str_dict convert dict to dict that value is str

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