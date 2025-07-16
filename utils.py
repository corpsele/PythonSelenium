import json
import platform
import os
import sys

# file_path = 'data.json'  # JSON文件路径
# data = read_json_file(file_path)
# print(data)  # 打印读取的数据
# print(type(data))  # 打印数据的类型

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

import platform

def get_os_from_platform():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    elif os_name == "Darwin":
        return "macOS"
    else:
        return os_name

import os

def get_os_from_os():
    if os.name == 'nt':
        return "Windows"
    elif os.name == 'posix':
        if os.uname()[0] == 'Linux':
            return "Linux"
        elif os.uname()[0] == 'Darwin':
            return "macOS"
        else:
            return "Unix或类Unix系统"
    else:
        return "未知操作系统"


