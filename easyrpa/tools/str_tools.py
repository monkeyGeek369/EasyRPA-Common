import json
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum


def str_is_empty(str):
    """str_is_empty judge str is empty

    Args:
        str (str): str

    Returns:
        bool: bool
    """
    if not str:
        return True
    if len(str) <= 0:
        return True
    return False

def str_is_not_empty(str):
    """str_is_not_empty judge str is not empty

    Args:
        str (str): str

    Returns:
        bool: bool
    """
    return not str_is_empty(str)

def dict_key_value_is_all_str(dic_item:dict):
    """check dict keys and values is all str type

    Args:
        dic_item (dict): params

    Returns:
        bool: is all str
    """
    if not dic_item or len(dic_item) <= 0:
        return False

    # 检查字典的所有键和值是否都是字符串类型
    keys_are_strings = all(isinstance(key, str) for key in dic_item)
    values_are_strings = all(isinstance(value, str) for value in dic_item.values())

    # 验证键和值都是字符串
    if keys_are_strings and values_are_strings:
        return True
    else:
        return False

def dict_key_value_is_not_all_str(dic_item:dict):
    """check dict keys and values is not all str type

    Args:
        dic_item (dict): params

    Returns:
        bool: is not all str
    """
    return not dict_key_value_is_all_str(dic_item)

def str_to_str_dict(param:str) -> dict:
    if not param:
        return None
    
    json_obj = None
    try:
        json_obj = json.loads(param)
    except:
        raise EasyRpaException("param is not json type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    
    for key, value in json_obj.items():
        json_obj[key] = str(value)

    return json_obj