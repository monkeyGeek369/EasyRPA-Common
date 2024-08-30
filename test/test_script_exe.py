import unittest
from easyrpa.script_exe import subprocess_python_script

class SubprocessScriptTest(unittest.TestCase):

    def test_subprocess_script(self):
        # 环境激活指令
        env_activate_command = 'source activate playwright'
        
        # 指定Python解释器名称，这里使用conda环境中的python
        python_interpreter = 'python3'
        
        # 外部Python脚本的文件路径
        script_path = '/test/test_script.py'
        
        # 传递给外部脚本的参数列表
        #params = '{\"key1\":\"value1\",\"key2\":True,\"key3\":{\"key31\":123}}'
        params = {"key1":"value1","key2":"value2","key3":"value3"}

        # 执行脚本并获取结果
        execution_result = subprocess_python_script.subprocess_script_run(env_activate_command, python_interpreter, script_path, params)
        
        # 打印执行结果
        if execution_result is not None:
            print("执行结果:", execution_result)

#unittest.main()作为主函数入口
if __name__ == '__main__':
    unittest.main()