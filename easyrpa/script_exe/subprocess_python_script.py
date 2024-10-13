from operator import truediv
import subprocess
from easyrpa.tools import str_tools,logs_tool
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.models.scripty_exe_result import ScriptExeResult
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
from easyrpa.enums.rpa_exe_result_code_enum import RpaExeResultCodeEnum
import os
import tempfile
from easyrpa.models.base.script_exe_param_model import ScriptExeParamModel
import platform

def subprocess_script_run(env_activate_command:str, python_interpreter:str 
                          ,script:str,dict_args:dict) -> ScriptExeResult:
    """
    激活环境后,使用指定的Python解释器执行外部Python脚本,并传递参数。
    注意事项：
    1、脚本执行结果通过print输出流获取，因此脚本中的输出内容编码必须为UTF-8（后端从输出流中解析使用utf-8），暂不支持指定其他编码。

    :param env_activate_command: 环境激活指令
    :param python_interpreter: 要使用的Python解释器的名称,如 'python'/'python3'。
    :param script: 外部Python脚本字符串
    :param dict_args: 传递给外部脚本的参数(字典对象),key与value必须是字符串类型
    :return: ScriptExeResult 外部脚本的执行结果(从print输出流获取)
    """

    # 创建一个临时文件
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py',encoding='utf-8') as tmpfile:
        filename = tmpfile.name
        tmpfile.write(script)
        tmpfile.flush()  # 确保内容写入文件
    try:

        # 基础校验
        if str_tools.str_is_empty(env_activate_command):
            raise EasyRpaException("env_activate_command is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
        if str_tools.str_is_empty(python_interpreter):
            raise EasyRpaException("python_interpreter is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
        if str_tools.str_is_empty(script):
            raise EasyRpaException("script is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
        if not dict_args or len(dict_args) <= 0:
            raise EasyRpaException("dict_args is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,script)
        if str_tools.dict_key_value_is_not_all_str(dict_args):
            raise EasyRpaException("dict_args kes and values is not all str",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,dict_args)

        # 构建conda激活命令和Python脚本执行命令
        command = f"{env_activate_command} && {python_interpreter} {filename}"

        # 更新环境变量
        env_vars = os.environ.copy()
        for key, value in dict_args.items():
            env_vars[key] = value

        result = None
        if platform.system() == "Windows":
            # 使用subprocess.run执行命令，捕获输出
            result = subprocess.run(
                command,
                env= env_vars, # 将外部脚本参数当作子流程变量传递,避免并发问题.注意字典的key和value必须是str,否则会有类型错误
                stdout=subprocess.PIPE,  # 创建一个管道来捕获输出
                stderr=subprocess.PIPE,  # 创建一个管道来捕获错误
                shell=True,        # 需要开启shell以执行conda激活命令
                text=True,           # true输出为文本格式,否则为字节方式输出
                encoding='utf-8',    # 设置输出编码
            )
        else:
            result = subprocess.run(
                ["/bin/bash", "-c", command],
                env= env_vars, # 将外部脚本参数当作子流程变量传递,避免并发问题.注意字典的key和value必须是str,否则会有类型错误
                stdout=subprocess.PIPE,  # 创建一个管道来捕获输出
                stderr=subprocess.PIPE,  # 创建一个管道来捕获错误
                shell=False,        # 需要开启shell以执行conda激活命令
                text=True,           # true输出为文本格式,否则为字节方式输出
                encoding='utf-8',    # 设置输出编码
            )
        
        # 获取保准异常输出流
        derr = None
        if str_tools.str_is_not_empty(result.stderr):
            derr = result.stderr

        # 获取标准输出流
        print_list = None
        if str_tools.str_is_not_empty(result.stdout):   
            stdout = result.stdout
            if str_tools.str_is_not_empty(stdout):
                print_list = stdout.splitlines(keepends=False)
        
        # 执行结果返回
        if print_list is None or len(print_list) < 0:
            return ScriptExeResult(True,derr,print_list,None,RpaExeResultCodeEnum.FLOW_EXE_DATA_ERROR.value[1])
        else:
            return ScriptExeResult(True,derr,print_list[:-1],print_list[-1],RpaExeResultCodeEnum.SUCCESS.value[1])
    except subprocess.CalledProcessError as cpe:
        logs_tool.log_script_error(title="subprocess_script_run",message="script run error",data=script,exc_info=cpe)
        return ScriptExeResult(False,cpe.stderr,None,None,RpaExeResultCodeEnum.SYSTEM_OPT_ERROR.value[1])
    except EasyRpaException as easye:
        logs_tool.log_script_error(title="subprocess_script_run",message="script run error",data=script,exc_info=easye)
        return ScriptExeResult(False,str(easye),None,None,RpaExeResultCodeEnum.FLOW_EXE_ERROR.value[1])
    except Exception as e:
        logs_tool.log_script_error(title="subprocess_script_run",message="script run error",data=script,exc_info=e)
        return ScriptExeResult(False,str(e),None,None,RpaExeResultCodeEnum.FLOW_EXE_ERROR.value[1])
    finally:
        # 删除临时文件
        os.remove(filename)

def script_exe_param_builder(param:ScriptExeParamModel) -> dict:
    """
    将ScriptExeParamModel转换为dict

    Args:
        param (ScriptExeParamModel): 请求参数

    Returns:
        dict: str dict
    """
    if not param:
        return None
    
    # 将类对象转换为json字符串
    json_str = param.to_json()

    # 将json字符串转换为dict
    dict_param = str_tools.str_to_str_dict(json_str)

    return dict_param

def env_activate_command_builder(flow_exe_env:str) -> str:
    """
    构建conda激活命令

    Args:
        env_activate_command (str): 环境激活指令

    Returns:
        str: conda激活命令
    """
    
    env_activate_command = None
    if platform.system() == "Windows":
        env_activate_command = f'conda activate {flow_exe_env}'
    elif platform.system() == "Linux":
        env_activate_command = f'source activate {flow_exe_env}'
    else:
        raise EasyRpaException("operation sysytem is not support",EasyRpaExceptionCodeEnum.SYSTEM_NOT_FOUND,None,flow_exe_env)

    return env_activate_command
    