from easyrpa.models.base.request_header import RequestHeader
from easyrpa.tools import thread_local
import uuid
from datetime import datetime

# 从请求中获取指定内容
def get_parameter(request, param, default, cast_type):
    #  先request.args 后request.form 然后转换cast_type=int|float类型。
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
