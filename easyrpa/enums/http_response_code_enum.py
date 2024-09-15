from enum import Enum

class HttpResponseCode(Enum):
    SUCCESS = (200, '成功')
    BAD_REQUEST = (400, '请求错误')
    UNAUTHORIZED = (401, '未授权')
    FORBIDDEN = (403, '禁止访问')
    NOT_FOUND = (404, '未找到')
    METHOD_NOT_ALLOWED = (405, '方法不允许')
    INTERNAL_SERVER_ERROR = (500, '内部错误')
    SERVICE_UNAVAILABLE = (503, '服务不可用')