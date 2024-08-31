import subprocess
from easyrpa.tools import str_tools
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.models.scripty_exe_result import ScriptExeResult
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
import os
import tempfile

def subprocess_script_run(env_activate_command:str, python_interpreter:str 
                          ,script:str,dict_args:dict):
    """
    激活环境后,使用指定的Python解释器执行外部Python脚本,并传递参数。

    :param env_activate_command: 环境激活指令
    :param python_interpreter: 要使用的Python解释器的名称,如 'python'/'python3'。
    :param script: 外部Python脚本字符串
    :param dict_args: 传递给外部脚本的参数(字典对象),key与value必须是字符串类型
    :return: ScriptExeResult 外部脚本的执行结果(从print输出流获取)
    """

    # 创建一个临时文件
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py') as tmpfile:
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

        # 使用subprocess.run执行命令，捕获输出
        result = subprocess.run(
            command,
            env= env_vars, # 将外部脚本参数当作子流程变量传递,避免并发问题.注意字典的key和value必须是str,否则会有类型错误
            stdout=subprocess.PIPE,  # 创建一个管道来捕获输出
            stderr=subprocess.PIPE,  # 创建一个管道来捕获错误
            shell=True,        # 需要开启shell以执行conda激活命令
            text=True           # 输出为文本格式,否则为字节方式输出
        )
        
        # 获取失败信息
        if result.stderr and str_tools.str_is_not_empty(result.stderr):
            return ScriptExeResult(False,"script exe error:" + result.stderr,None,None)

        # 获取标准输出流
        print_list = None
        if result.stdout and str_tools.str_is_not_empty(result.stdout):   
            print_list = result.stdout.splitlines(keepends=False)
        
        # 执行结果返回
        if not print_list or len(print_list) < 0:
            return ScriptExeResult(False,"script exe result is empty",None,None)
        else:
            return ScriptExeResult(True,"script exe success",print_list[:-1],print_list[-1])
    except subprocess.CalledProcessError as cpe:
        return ScriptExeResult(False,cpe.stderr,None,None)
    except EasyRpaException as easye:
        return ScriptExeResult(False,str(easye),None,None)
    except Exception as e:
        return ScriptExeResult(False,str(e),None,None)
    finally:
        # 删除临时文件
        os.remove(filename)
