from dataclasses import dataclass
from easyrpa.models.base.request_header import RequestHeader


@dataclass
class ScriptExeParamModel:
    """外部脚本执行参数模型

    Args:
        env_activate_command (str): 环境激活指令
        python_interpreter (str): 要使用的Python解释器的名称，如 'python'/'python3'。
        script (str): 外部Python脚本字符串
        dict_args (dict): 传递给外部脚本的参数（字典对象），key与value必须是字符串类型
    """
    header: RequestHeader
    source: int
    standard: dict
    flow_config:dict