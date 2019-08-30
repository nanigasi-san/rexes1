import json

json_path = "inp/2stream.json"
with open(json_path,"r") as f:
    param_dic = json.loads(f.read())

global_param = param_dic["global"]
particle_param_tuple = tuple([item[1] for item in list(param_dic.items())[1:]])