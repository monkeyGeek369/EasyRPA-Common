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
    """将json字符串转换为dict，递归完成对所有层级value值转换为str类型

    Args:
        param (str): json字符串

    Raises:
        EasyRpaException: 异常信息

    Returns:
        dict: 字典结果
    """
    if not param:
        return None
    
    json_obj = None
    try:
        json_obj = json.loads(param)
    except:
        raise EasyRpaException("param is not json type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    
    if isinstance(json_obj, list):
        # 遍历json数组
        list_tmp = []
        for item in json_obj:
            json_item = str_to_str_dict(json.dumps(item))
            list_tmp.append(json_item)
        json_obj = list_tmp
    elif isinstance(json_obj,dict):
        # 便利json对象
        for key, value in json_obj.items():
            # 如果是字符串类型则无需处理
            if isinstance(value, str):
                continue

            # 如果是json对象则需要再次便利内部对象进行转换
            if isinstance(value, dict):
                json_obj[key] = str_to_str_dict(json.dumps(value))
                continue

            # 如果是json数组则需要再次便利内部对象进行转换
            if isinstance(value, list):
                list_tmp = []
                for item in value:
                    json_item = str_to_str_dict(json.dumps(item))
                    list_tmp.append(json_item)
                json_obj[key] = list_tmp
                continue

            # 其它类型默认转换（布尔类型、None类型、数字类型）
            json_obj[key] = str(value)
    else:
        json_obj = str(json_obj)

    return json_obj

def str_to_dict_first_level(param:str) -> dict:
    """将json字符串转换为dict，只针对第一层级value值转换为str类型

    Args:
        param (str): json字符串

    Raises:
        EasyRpaException: 异常信息

    Returns:
        dict: 字典结果
    """
    if not param:
        return None
    
    json_obj = None
    try:
        json_obj = json.loads(param)
    except:
        raise EasyRpaException("param is not json type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,param)
    
    if isinstance(json_obj, list):
        # 遍历json数组
        list_tmp = []
        for item in json_obj:
            json_item = str_to_dict_first_level(json.dumps(item))
            list_tmp.append(json_item)
        json_obj = list_tmp
    elif isinstance(json_obj,dict):
        # 将所有value转换为str
        for key, value in json_obj.items():
            json_obj[key] = str(value)
    else:
        json_obj = str(json_obj)

    return json_obj
