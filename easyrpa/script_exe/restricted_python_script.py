
def execute_script(script:str, script_data:dict):
    """
    执行外部Python脚本字符串。
    
    :param script: 要执行的Python脚本字符串。
    :param data: 要在脚本中使用的字典，作为脚本的全局变量。
    :return: 
    """

    # 创建一个字典来保存脚本的全局变量
    global_vars = script_data.copy()
    
    # 编译脚本为字节码
    try:
        byte_code = compile(script, '<string>', 'exec')
    except SyntaxError as e:
        print(f"Syntax error in script: {e}")
        return None
    
    # 执行脚本
    try:
        exec(byte_code, global_vars)
    except Exception as e:
        print(f"Error executing script: {e}")
        return None
    
    # 返回脚本执行影响的全局变量
    return global_vars