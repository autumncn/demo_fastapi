import json

from fastapi import Depends

from db import crud
from db.database import get_db


def dict_to_json(dict_input):
    json_output = json.dumps(dict_input, indent=4)
    return json_output


def json_to_dict(json_input):
    output_dict = json.loads(json_input)
    return output_dict

def objetc_to_json(object_input):
    # 使用 dumps函数直接将对象转化为JSON结果
    # ensure_ascii 默认为True，会将汉字转换为ascii码
    result = json.dumps(object_input,ensure_ascii = False)
    return result

def model_list(result):
    list = []
    for row in result:
        dict = {}
        for k,v in row.__dict__.items():
            if not k.startswith('_sa_instance_state'):
                dict[k] = v
        list.append(dict)
    return list

if __name__ == '__main__':
    dict_input = {"name": "zhangsan", "age": 18}
    json_output = dict_to_json(dict_input)
    print("字典转json的结果: ", json_output)

    json_input = '{"name": "zhangsan", "age": 18}'
    output_dict = json_to_dict(json_input)
    print("json转字典的结果: ", output_dict)

    object_input = {"name": "zhangsan", "age": 18}
    result = objetc_to_json(object_input)
    print("对象转json的结果: ", result)


