import subprocess
import ast
from typing import List
from tools import str_tools
from models.easy_rpa_exception import EasyRpaException
from models.scripty_exe_result import ScriptExeResult
from enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum

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
    if not dict_args or len(dict_args):
        raise EasyRpaException("dict_args is empty",EasyRpaExceptionCodeEnum.DATA_NULL,None,script_path)

    # 构建conda激活命令和Python脚本执行命令
    command = f"{env_activate_command} && {python_interpreter} {script_path}"
    
    try:
        # 使用subprocess.run执行命令，捕获输出
        result = subprocess.Popen(
            command,
            env= dict_args, # 将外部脚本参数当作子流程变量传递,避免并发问题
            shell=True,        # 需要开启shell以执行conda激活命令
            capture_output=True,  # 捕获输出
            text=True,           # 输出为文本格式,否则为字节方式输出
            check=True           # 将非零返回码视为异常
        )
        
        # 获取标准输出流
        print_list = result.stdout.readlines

        if not print_list or len(print_list):
            return ScriptExeResult(False,"")

        return ScriptExeResult
    except subprocess.CalledProcessError as e:
        # 打印错误信息
        print(f"An error occurred: {e}")
        return None

def prints_to_result(prints:str)


# 使用示例
if __name__ == "__main__":
    # Conda环境名称
    conda_env_name = 'playwright'
    
    # 指定Python解释器名称，这里使用conda环境中的python
    python_interpreter = 'python3'
    
    # 外部Python脚本的文件路径
    script_path = 'test.py'
    
    # 传递给外部脚本的参数列表
    #params = '{\"key1\":\"value1\",\"key2\":True,\"key3\":{\"key31\":123}}' # 替换为实际参数
    params = {"key1":"value1","key2":True,"key3":{"key31":123}}

    # 执行脚本并获取结果
    execution_result = run_external_python_script(conda_env_name, python_interpreter, script_path, params)
    
    # 打印执行结果
    if execution_result is not None:
        python_dict = ast.literal_eval(execution_result)
        print("Execution result:", execution_result)