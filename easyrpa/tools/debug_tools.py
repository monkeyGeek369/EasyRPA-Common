from easyrpa.models.base.script_exe_param_model import ScriptExeParamModel
from easyrpa.tools import request_tool
from easyrpa.tools.str_tools import dict_key_value_is_not_all_str
from easyrpa.tools.transfer_tools import any_to_str_dict_first_level
import json
from dataclasses import asdict
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
import os
from easyrpa.models.base.request_header import RequestHeader

def env_params_build(header:RequestHeader,sub_source:int,flow_standard_message:str,flow_config:str) ->dict:
    """构建环境参数

    Args:
        header (RequestHeader): 请求头
        sub_source (int): 来源
        flow_standard_message (str): 流程标准消息
        flow_config (str): 流程配置

    Returns:
        dict: 环境参数
    """

    script_param = ScriptExeParamModel(header=(header if header else request_tool.get_current_header())
                                       ,source=sub_source
                                       ,standard=flow_standard_message
                                       ,flow_config=flow_config)
    
    dict_data = asdict(script_param)
    return any_to_str_dict_first_level(json.dumps(dict_data,default=str))

def set_envs_by_params(params:dict):
    """设置环境变量

    Args:
        params (dict): 环境变量参数

    Raises:
        EasyRpaException: 异常信息
    """
    if not params or len(params) <= 0:
        raise EasyRpaException("dict_args is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,params)
    if dict_key_value_is_not_all_str(params):
        raise EasyRpaException("dict_args kes and values is not all str",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,params)
    
    # 更新环境变量
    for key, value in params.items():
        os.environ[key] = value

def env_params_build_and_set(header:RequestHeader,sub_source:int,flow_standard_message:str,flow_config:str):
    """环境参数构建和设置

    Args:
        sub_source (int): 来源
        flow_standard_message (str): 流程标准消息
        flow_config (str): 流程配置
    """

    # 构建环境参数
    params = env_params_build(header=header,sub_source=sub_source,flow_standard_message=flow_standard_message,flow_config=flow_config)
    # 设置环境变量
    set_envs_by_params(params)