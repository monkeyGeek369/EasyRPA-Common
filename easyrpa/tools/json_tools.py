import json
from datetime import datetime
from easyrpa.models.base.script_exe_param_model import ScriptExeParamModel
from easyrpa.models.base.request_header import RequestHeader

class JsonTool:
    @staticmethod
    def obj_to_json(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.dumps(obj, default=lambda o: o.__dict__)

    @staticmethod
    def json_to_obj(json_str, obj_class):
        data = json.loads(json_str)
        return obj_class(**data)
    
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
    json_str = JsonTool.obj_to_json(obj)
    print(json_str)