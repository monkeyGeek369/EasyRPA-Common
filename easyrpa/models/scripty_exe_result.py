from typing import List
class ScriptExeResult:
    def __init__(self,status:bool,error_msg:str,print_str:List[str],result:str):
        self.status = status
        self.error_msg = error_msg
        self.print_str = print_str
        self.result = result