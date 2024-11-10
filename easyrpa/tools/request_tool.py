from easyrpa.models.base.request_header import RequestHeader
from easyrpa.tools import thread_local
import uuid
from datetime import datetime
from easyrpa.tools import logs_tool
import functools
from flask import request
from easyrpa.enums.http_response_code_enum import HttpResponseCode
from easyrpa.models.base.response_base_model import ResponseBaseModel
from easyrpa.models.base.request_base_model import RequestBaseModel
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
from easyrpa.tools.json_tools import JsonTool

# 
def get_parameter(request, param, default, cast_type):
    """从请求中获取指定内容(先request.args 后request.form 然后转换cast_type=int|float类型)

    Args:
        request (_type_): 请求对象
        param (_type_): 参数
        default (_type_): 默认值
        cast_type (_type_): 转换类型

    Returns:
        _type_: 返回值
    """
    #  
    for method in [request.args.get, request.form.get]:
        value = method(param, "").strip()
        if value:
            try:
                return cast_type(value)
            except ValueError:
                break  # args转换失败，退出尝试form
    return default  # 失败，返回默认值。

def get_current_header() -> RequestHeader:
    """get request header model

    Returns:
        RequestHeader: RequestHeader
    """
    header = thread_local.get_thread_local_data().get_data("header")
    if not header:
        result_header = RequestHeader(user_id=1,trace_id=str(uuid.uuid4()),req_time=datetime.now())
        thread_local.get_thread_local_data().set_data("header",result_header)
    
    return thread_local.get_thread_local_data().get_data("header")

def set_current_header(header:RequestHeader):
    """设置当前环境header

    Args:
        header (RequestHeader): header
    """
    thread_local.get_thread_local_data().set_data("header",header)

def easyrpa_request_wrapper(func):
    """对接口使用装饰器

    Args:
        func (_type_): 接口函数

    Raises:
        e: 异常信息

    Returns:
        _type_: 返回结果
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # 记录请求内容
            logs_tool.log_api_info(title="request_data_record",message=func.__name__,data=request.get_json())

            # 获取请求model
            origin_model = request.get_json()
            if origin_model is None:
                raise EasyRpaException("request model is null",EasyRpaExceptionCodeEnum.DATA_NULL.value[1],None,origin_model)
            
            req_model = None
            if isinstance(origin_model,dict):
                header = RequestHeader(**origin_model['header'])
                req_model = RequestBaseModel(header=header, model=origin_model['model'])
            elif isinstance(origin_model,str):
                req_model = get_request_base_model(origin_model)
            else:
                raise EasyRpaException("request model type error",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR.value[1],None,origin_model)

            # 获取header
            req_header = req_model.header
            if req_header is None:
                raise EasyRpaException("request header is null",EasyRpaExceptionCodeEnum.DATA_NULL.value[1],None,req_model)

            # 设置header
            set_current_header(req_header)
            
            # 调用原始视图函数
            response = func(req_model.model)
            
            # 返回响应
            res_model = ResponseBaseModel(status=True
                                          ,code=HttpResponseCode.SUCCESS.value[0]
                                          ,message=HttpResponseCode.SUCCESS.value[1]
                                          ,data=response)
            res_result = JsonTool.any_to_dict(res_model)

            # 记录响应内容
            logs_tool.log_api_info(title="request_response_record",message=func.__name__,data=res_result)
            
            return res_result
        except Exception as e:
            # 返回响应
            res_error = ResponseBaseModel(status=False
                                          ,code=HttpResponseCode.BAD_REQUEST.value[0]
                                          ,message=HttpResponseCode.BAD_REQUEST.value[1]
                                          ,data=e.__dict__ if hasattr(e,'__dict__') and len(e.__dict__)>0 else e.args
                                          )
            res_result = JsonTool.any_to_dict(res_error)

            # 记录错误内容
            logs_tool.log_api_error(title="request_error_record",message=func.__name__,data=res_result,exc_info=e)

            return res_result
    return wrapper

def request_base_model_builder(model:any) -> RequestBaseModel:
    return RequestBaseModel(header=get_current_header(),model=model)

def request_base_model_json_builder(model:any) -> str:
    return JsonTool.any_to_json(request_base_model_builder(model))

def get_request_base_model(json_str:str) -> RequestBaseModel:
    dict_dto = JsonTool.any_to_dict(json_str)
    
    ret = RequestBaseModel(
        header=RequestHeader(**dict_dto.get('header')),
        model=dict_dto.get('model')
    )

    return ret

def get_request_base_model_data(json_str:str) -> any:
    return get_request_base_model(json_str).model
