#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""=================================================
@Desc   ：主接口
=================================================="""
import os
import random
import time

from colors import ColorMultiImage
import settings
from model import training
import csv
from pymongo import MongoClient
import datetime
import sys


nftSeriesId = settings.chooesId


def login(temp):
    nftSeries = []
    for i in temp:
        nftSeries.append(list(i.values())[0])
    print('>>> 【NFT自动生成程序】启动成功')
    print('>>>  启动成功')
    print(f'>>> 训练集存放路径: {settings.color_data_path}')
    print(f'>>> 默认生成数量: {settings.food_num}')
    print(f'>>> 默认作品风格: {settings.color_style} (0为随机风格，1为艺术家风格)')
    print(f'>>> 默认生成算法: Means算法分成K类')
    print(f'>>> 默认艺术家风格分箱颜色数: {settings.random_state} (数量越多色彩越鲜艳)')
    print(f'>>> 默认艺术家风格颜色差异距离检查数: {settings.color_distance} (作品色彩差异度)')
    print(f'>>> 默认训练模型生成路径: {settings.color_model_path} (使用自动训练后生成模型参数的存放路径)')
    print(f'>>> 默认生成模式: {settings.train} 0：自动训练模型 1：使用已有训练集')
    print('\n目前已生成NFT系列：')
    for i in range(len(nftSeries)):
        print(f'{i + 1}. {nftSeries[i]}')
    # exit()
    return choose(len(nftSeries))


def choose(maxNum):
    global nftSeriesId
    nums = [i + 1 for i in range(maxNum)]
    while True:
        nftSeriesId = int(input("请选择要生成的系列作品ID(输入0则生成全部系列作品)："))
        num = input("请输入生成数量(无输入将默认生成10个)：")
        models = input("请输入生成模式(0:训练模式 1:生成模式 无输入将使用自动训练模型)：")
        if num != '':
            settings.food_num = int(num)
        if models != '':
            if models == 1:
                settings.train = True
            elif models == 0:
                settings.train = False
            else:
                print('无此模式，将采用默认模型')
        if nftSeriesId != 0:
            if nftSeriesId not in nums:
                print(f'您输入的系列不存在，请输入0-{maxNum}之间的数字')
            else:
                return False
        if nftSeriesId == 0:
            return True
    return True


def nftCore(cout):
    global stickers
    print('>>>当前用户要生成的作品数量为：' + str(settings.food_num))
    print('>>>' + '开始生成..')
    for amount in range(0, settings.food_num):  # 设置生成数量

        pixel = generate_color.merges(stickers[:2])

        colors_number = generate_color.colors_number
        generate_color.generate(pixel, settings.color_output_name, str(cout), settings.color_model_path,
                                settings.color_style, colors_number)
        print(f"{str(cout)}.正在生成第{str(amount + 1)}个作品")
        cout += 1
    print()
    return cout


def nftCore2(cout):
    print('>>>当前用户要生成的作品数量为：' + str(settings.food_num))
    print('>>>' + '开始生成..')
    t = []
    for amount in range(0, settings.food_num):  # 设置生成数量
        t.append(stickers[0])
        t.append(stickers[settings.chooesId])
        pixel = generate_color.merges(t)

        colors_number = generate_color.colors_number
        generate_color.generate(pixel, settings.color_output_name, str(amount), settings.color_model_path,
                                settings.color_style, colors_number)
        print(f"{str(cout)}.正在生成第{str(amount + 1)}个作品")
        cout += 1
    print()
    return cout


def nftCore3():
    for amount in range(0, settings.food_num):  # 设置生成数量
        pixel = generate_color.merges(stickers)
        colors_number = generate_color.color_number
        generate_color.generate(pixel, settings.color_output_name, str(amount), settings.color_model_path,
                                settings.color_style, colors_number)
        print(f"INFO:生成第{str(amount)}个{settings.color_output_name}")


def toMongo():
    print('>>>开始连接MongoDB数据库...')
    # host = '103.139.1.219'
    host = '127.0.0.1'
    client = MongoClient(host, 27017)
    newNtf1 = client["newNtf1"]
    foods = newNtf1["foods"]
    print('foods:')
    print(foods)
    
    classifications = newNtf1['categories']
    
    print('classifications:')
    print(classifications)
    for i in classifications.find():
        print(i)
    print('>>>数据库连接成功，能找到对应的表...')
    insertClassifications(classifications, readimagesURL())
    insertFoods(foods, classifications)
    print('>>>关闭MongoDB连接')
    client.close()


def redom_nums(starts, end, space, add):
    if add is None:
        add = 0
    prices = []
    for i in range(30):
        prices.append(random.randint(starts - space + add, end + space + add))
    return prices


def insertClassificationsDate(classifications, name, img_url):
    flag = 1
    # todo
    # removeAll(classifications)
    for i in name:
        print('插入一条分类数据')
        classifications_query = {"name": i}
        query = classifications.find(classifications_query)
        query_temp = []
        for t in query:
            query_temp.append(t)
        if len(query_temp) == 0:
            classifications.insert_one(
                {
                    'name': i,
                    'imgUrl': f'http://www.fortis.ink:8801/upload/{settings.color_output_name}/{flag}.png',
                    'nowPrice': redom_nums(settings.starts, settings.end, settings.space, settings.add),
                    'quantity': 0,
                    'batch': 1
                }
            )
        flag += 1
    print('>>>分类插入成功，共插入了' + str(flag) + '条数据')
    print('>>>当前已成功生成的分类数据：')
    classifications_find = classifications.find({'batch': 1})
    for i in classifications_find:
        print(i)


def insertClassifications(classifications, img_url):
    print('>>>开始插入分类数据')
    if settings.chooesId != (len(settings.module)):
        print('>>>用户选择了单分类，要插入一个分类')
        module_name = list(settings.module[1:][settings.chooesId - 1].values())[0]
        print('>>>插入的分类为：' + module_name)
        insertClassificationsDate(classifications, [module_name], img_url)
    else:
        print('>>>用户选了全部系列分类，插入一堆分类')
        classifications_names = []
        for i in settings.module[1:]:
            classifications_names.append(list(i.values())[0])
        insertClassificationsDate(classifications, classifications_names, img_url)


def removeAll(c):
    c.delete_many({'batch': 1})
    

def readimagesURL():
    path = f'../static/upload/{settings.color_output_name}'  # 输入文件夹地址
    print('imgURL：' + path)
    files = os.listdir(path)  # 读入文件夹
    num_png = len(files) - 1  # 统计文件夹中的文件个数
    # print(num_png)  # 打印文件个数

    imagesURL = []

    for imageURL in files:
        imagesURL.append(f'http://www.fortis.ink:8801/upload/{settings.color_output_name}/{imageURL}')
    return imagesURL


def test(conectiong):
    find = conectiong.find({'batch': 1})
    for i in find:
        print(i)
    exit()


def insertFoodsData(foods, classifications_ids):
    # todo
    # removeAll(foods)
    print('>>>开始插入商品数据...')
    flag = 1
    for i in classifications_ids:

        for j in range(settings.food_num):
            print('插入一条商品数据')
            foods.insert_one(
                {
                    'name': settings.food_name + '#00' + str(flag),
                    'imgUrl': f'http://www.fortis.ink:8801/upload/{settings.color_output_name}/{flag-1}.png',
                    'classification': {
                        '$oid': {i}
                    },
                    'stratPrice': settings.starts,
                    'introduce': settings.food_notes,
                    'nowPrice': redom_nums(settings.starts, settings.end, settings.space, settings.add),
                    'config': {
                        'starts': settings.starts,
                        'end': settings.end,
                        'space': settings.space,
                        'add': settings.add
                    },
                    'isShow': settings.isShow,
                    'userSell': [],
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'SWI': True,
                    'batch': 1
                }
            )
            flag += 1
    print('>>>商品数据插入成功...共插入' + str(flag - 1) + '条数据...')
    print('>>>当前成功生成的商品数据！')
    for i in foods.find({'batch': 1}):
        print(i)


def insertFoods(foods, classifications):
    print('>>>开始插入商品数据...')

    classifications_ids = []

    if settings.chooesId != (len(settings.module)):
        print('>>>单系列分类商品数据')
        classifications_query = classifications.find({'name': settings.module[1:][settings.chooesId-1]['name']})
        for j in classifications_query:
            classifications_ids.append(str(j['_id']))
        insertFoodsData(foods, classifications_ids)

    else:
        print('>>>全系列分类商品数据')

        for i in settings.module[1:]:
            classifications_query = classifications.find({'name': list(i.values())[0]})
            for j in classifications_query:
                classifications_ids.append(str(j['_id']))

        insertFoodsData(foods, classifications_ids)


if __name__ == '__main__':
    if settings.app_start:
        exit()
    else:

        start_time = time.time()
        print('>>>' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('>>>' + "filepath:", __file__, "\nfilename:", os.path.basename(__file__))
        print('>>>' + 'NFT自动化生成程序开始启动...')
        print('>>>' + '>>>输出配置信息')
        print(settings)
        print('>>>' + '输出用户输入')

        generate_color = ColorMultiImage()
        stickers = settings.module
        stickers_temp = stickers[1:]

        cout = 1
        if settings.train:
            color_model_path = training(settings.color_data_path)
            print("颜色模型生成路径:" + color_model_path)
        if settings.color_style == 1:
            f = open(settings.color_model_path, "r+", encoding="utf-8-sig")
            reader = csv.reader(f)
            colors_max = len(list(reader))
        print(f"{settings.color_output_name}项目:")
        if nftSeriesId == len(settings.module) - 1:
            # 全部分类生成
            print('>>>' + '当前用户选择生成【全部系列】作品')
            for i in stickers_temp:
                stickers[1] = i
                print(f"正在生成{list(i.values())[0]}系列作品：")
                cout = nftCore(cout)
        else:
            # 生成单系列
            print('当前用户选择生成【单系列】作品')
            print(f"正在生成{list(stickers_temp[nftSeriesId - 1].values())[0]}系列作品：")
            cout = nftCore2(cout)

        if settings.color_style == 1:
            print(f"当前为艺术家风格，当前模型可用颜色数为{colors_max}个")
        else:
            print(f"当前为随机风格，当前模型可用颜色数为256个")
        if nftSeriesId == 0:
            print(f"{str(len(stickers_temp))}个系列总计{str(cout - 1)}个作品生成完成")
        else:
            print(f"作品存放路径：{os.getcwd()}\\output\\{settings.color_output_name}")

        print('>>>作品生成完毕...')
        print('-----------------')
        toMongo()
        end_time = time.time()
        print('>>>本程序执行完毕,共用时：' + str(end_time - start_time) + 's')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

    exit()
