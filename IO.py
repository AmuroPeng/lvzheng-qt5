# -*- coding: utf-8 -*-

import json


def load_data():
    with open('data.json', 'r') as json_file:
        load_dict = json.load(json_file)
        print(str('###导入data.json数据###\t' + str(load_dict)))
    return load_dict


# def load_txt(load_path='data.txt'):
#     x_list = []
#     y_list = []
#     with open(load_path, 'r') as f:
#         for line in f.readlines():
#             line = str(line.strip())  # 把末尾的'\n'删掉
#             x_list.append(line.split(',')[0])
#             y_list.append(line.split(',')[1])
#         print(str('###导入data.txt数据###\t' + str(x_list)))
#         print(str('###导入data.txt数据###\t' + str(y_list)))
#     return x_list, y_list


def save_result_to_json(dic):
    json_str = json.dumps(dic)
    print(json_str)
    with open('/result/data.json', 'w') as json_file:
        save_dict = json.load(json_file)
        print(str('###导出data.json数据###\t' + str(save_dict)))


def save_result_to_txt(dic):
    with open(r'./检测结果/检测结果.txt', 'w') as f:
        f.write(str(dic))
    print(str('###导出 检测结果.txt 数据###\t' + str(dic)))


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
