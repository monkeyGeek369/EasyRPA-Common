import json
import dataclasses
import inspect
from datetime import datetime
from easyrpa.models.base.script_exe_param_model import ScriptExeParamModel
from easyrpa.models.base.request_header import RequestHeader
from easyrpa.models.agent_models.flow_task_exe_req_dto import FlowTaskExeReqDTO
from easyrpa.models.easy_rpa_exception import EasyRpaException
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum

class JsonTool:

    @staticmethod
    def serialize_object(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif callable(obj):
            return obj.__name__
        else:
            return obj
        
    @staticmethod
    def is_custom_class_instance(obj):
        cls = type(obj)
        module = inspect.getmodule(cls)
        return module is not None and module.__name__ != 'builtins'
        
    @staticmethod
    def obj_to_json(obj) -> str:
        if obj is None:
            return None
        if not JsonTool.is_custom_class_instance(obj):
            raise EasyRpaException("param is not custom class object",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,obj)
        if isinstance(obj, list):
            raise EasyRpaException("param is list type,not support",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,obj)
        obj_dict = dataclasses.asdict(obj)
        return json.dumps(obj_dict, default=JsonTool.serialize_object)
    
    @staticmethod
    def objs_to_json(objs) -> str:
        if objs is None:
            return None
        if not isinstance(objs, list):
            raise EasyRpaException("param is not list type",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,objs)
        
        temp_objs = []
        for obj in objs:
            if not JsonTool.is_custom_class_instance(obj):
                raise EasyRpaException("list obj is not custom class object",EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR,None,obj)
            if obj is not None:
                temp_objs.append(obj)
        
        return json.dumps([dataclasses.asdict(item) for item in temp_objs],default=JsonTool.serialize_object)
    
    
if __name__ == "__main__":
    header = RequestHeader(
        user_id=1,
        trace_id="sdfsgdggfhfh",
        req_time=datetime.now()
        )
    obj = ScriptExeParamModel(
        header=header,
        source=1,
        standard="standard",
        flow_config="flow_config"
    )

    objs = []
    objs.append(obj)
    objs.append(None)
    objs.append(obj)

    flow_task = FlowTaskExeReqDTO(
        task_id = 1,
        site_id = 2,
        flow_id = 3,
        flow_code = "flow_code",
        flow_name = "flow_name",
        flow_rpa_type = 4,
        flow_exe_env = 5,
        flow_standard_message = "",
        flow_exe_script = None,
        sub_source = 6
    )

    # obj to json
    json_str = JsonTool.obj_to_json(obj=obj)
    print(json_str)
    #json_str = JsonTool.obj_to_json(obj=objs)
    #print(json_str)
    #json_str = JsonTool.obj_to_json(obj=None)
    #print(json_str)
    #json_str = JsonTool.obj_to_json(obj="test")
    #print(json_str)
    #json_str = JsonTool.obj_to_json(obj=False)
    #print(json_str)
    json_str = JsonTool.obj_to_json(obj=flow_task)
    print(json_str)

    # objs to json
    json_str = JsonTool.objs_to_json(objs=objs)
    print(json_str)

    # dict to json

    # any to json

