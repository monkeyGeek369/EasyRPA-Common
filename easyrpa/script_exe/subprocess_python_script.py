import subprocess
from easyrpa.tools import str_tools
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.models.scripty_exe_result import ScriptExeResult
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum

def subprocess_script_run(env_activate_command:str, python_interpreter:str, script_path:str, dict_args:dict):
    """
    激活环境后,使用指定的Python解释器执行外部Python脚本,并传递参数。

    :param env_activate_command: 环境激活指令
    :param python_interpreter: 要使用的Python解释器的名称,如 'python'/'python3'。
    :param script_path: 外部Python脚本的文件路径
    :param dict_args: 传递给外部脚本的参数(字典对象)
    :return: 外部脚本的执行结果(命令行输出流),如果执行失败则返回None。
    """

    # 基础校验
    if str_tools.str_is_empty(env_activate_command):
        raise EasyRpaException("env_activate_command is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
    if str_tools.str_is_empty(python_interpreter):
        raise EasyRpaException("python_interpreter is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
    if str_tools.str_is_empty(script_path):
        raise EasyRpaException("script_path is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,dict_args)
    if not dict_args or len(dict_args) <= 0:
        raise EasyRpaException("dict_args is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,script_path)

    # 构建conda激活命令和Python脚本执行命令
    command = f"{env_activate_command} && {python_interpreter} {script_path}"
    
    try:
        # 使用subprocess.run执行命令，捕获输出
        result = subprocess.Popen(
            command,
            env= dict_args, # 将外部脚本参数当作子流程变量传递,避免并发问题.注意字典的key和value必须是str,否则会有类型错误
            stdout=subprocess.PIPE,  # 创建一个管道来捕获输出
            stderr=subprocess.PIPE,  # 创建一个管道来捕获错误
            shell=True,        # 需要开启shell以执行conda激活命令
            universal_newlines=True           # 输出为文本格式,否则为字节方式输出
        )
        
        # 获取标准输出流
        stdout, stderr = result.communicate()

        # todo mahao

        print_list = stdout.readlines

        # 执行结果返回
        if not print_list or len(print_list) < 0:
            return ScriptExeResult(False,"script exe result is empty",None,None)
        else:
            return ScriptExeResult(True,"script exe success",print_list[:-1],print_list[-1])
    except Exception as e:
        return ScriptExeResult(False,e.output,None,None)
