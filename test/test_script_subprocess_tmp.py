import subprocess
import os
import tempfile
import json

code = """
import json
from playwright import sync_api
import sys
import os

def print_json(data):
    print(json.dumps(data))

print_json({"message": "123"})

env_var1 = os.getenv('key1', 'Default Value')
print(f"The value of MY_ENV_VAR is: {env_var1}")
env_var2 = os.getenv('key2', 'Default Value')
print(f"The value of MY_ENV_VAR is: {env_var2}")
env_var3 = os.getenv('key3', 'Default Value')
print(f"The value of MY_ENV_VAR is: {env_var3}")

def test():
    print_json({"len": len(sys.argv), "args": sys.argv})
print_json({"message": "456"})
test()
print_json({"message": "78\\n9"})
"""

code2 = """
from playwright import sync_api
import sys

print("123")

def test():
    print(len(sys.argv))
    print(sys.argv)
print("456")
test()
print("789")
"""


# 创建一个临时文件
with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py') as tmpfile:
    filename = tmpfile.name
    tmpfile.write(code)
    tmpfile.flush()  # 确保内容写入文件

command = f'conda activate playwright && python {filename}'
env_vars = os.environ.copy()
env_vars['key1'] = 'Hello World1'
env_vars['key2'] = 'Hello World2'
env_vars['key3'] = 'Hello World3'

# 使用subprocess.run执行临时文件
try:
    result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env= env_vars)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # 解析输出
    outputs = result.stdout.splitlines(keepends=False)
    print("Parsed Outputs:", outputs)
    #parsed_outputs = [json.loads(line) for line in outputs]
    #print("Parsed Outputs:", parsed_outputs)
finally:
    # 删除临时文件
    os.remove(filename)