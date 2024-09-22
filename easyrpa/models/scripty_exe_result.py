from typing import List
from dataclasses import dataclass

@dataclass
class ScriptExeResult:
    status:bool
    error_msg:str
    print_str:List[str]
    result:str
    code:str