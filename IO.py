# -*- coding: utf-8 -*-

import json


def load_data():
    with open('data.json', 'r') as json_file:
        load_dict = json.load(json_file)
        print(str('###导入data.json数据###\t' + str(load_dict)))
        # todo: !!! for循环遍历load_dict把数据print在导入数据栏里
    return load_dict


def save_result(dic):
    json_str = json.dumps(dic)
    print(json_str)
    with open('/result/data.json', 'w') as json_file:  # todo: 最后一步 改输出，把所有数据+三张图片导出到根目录
        save_dict = json.load(json_file)
        print(str('###导出data.json数据###\t' + str(save_dict)))


def load_cache(filename):
    with open('/cache/{}.json'.format(filename), 'r') as json_file:
        load_dict = json.load(json_file)
        print(str('###导入{}数据###\t'.format(filename) + str(load_dict)))
    return load_dict


def save_cache(filename, dic):
    json_str = json.dumps(dic)
    print(json_str)
    with open('/cache/{}.json'.format(filename), 'w') as json_file:
        save_dict = json.dump(json_file)
        print(str('###导出{}数据###\t'.format(filename) + str(save_dict)))
