import unittest
from easyrpa.script_exe import subprocess_python_script

class SubprocessScriptTest(unittest.TestCase):

    def test_subprocess_script(self):
        # 环境激活指令
        env_activate_command = 'conda activate playwright'
        
        # 指定Python解释器名称，这里使用conda环境中的python
        python_interpreter = 'python'
        
        script = """
import json
from playwright import sync_api
import sys
import os

def print_json(data):
    print(json.dumps(data))

print_json({"message": "123"})

env_var1 = os.getenv('key1', 'Default Value')
print(f"{env_var1}")
env_var2 = os.getenv('key2', 'Default Value')
print(f"{env_var2}")
env_var3 = os.getenv('key3', 'Default Value')
print(f"{env_var3}")

def test():
    print_json({"len": len(sys.argv), "args": sys.argv})
print_json({"message": "456"})
test()
print_json({"message": "78\\n9"})
            """
        
        # 传递给外部脚本的参数列表
        params = {"key1":"value1","key2":"value2","key3":123}

        # 执行脚本并获取结果
        execution_result = subprocess_python_script.subprocess_script_run(env_activate_command, python_interpreter,script, params)
        
        # 打印执行结果
        if execution_result is not None:
            print("执行结果:", execution_result)

#unittest.main()作为主函数入口
if __name__ == '__main__':
    unittest.main()