#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Desc   ： 基础配置文件
========================================d=========="""
import function.subject as subject

color_data_path= './data/Monet/'  # 训练集文件夹路径
DATACENTER_ID= 0
WORKER_ID= 0
SEQUENCE= 0
color_model_path= "output/csv/1655963781118820352.csv"
module= [subject.canvas2, subject.cattle, subject.mouse, subject.cattle_DC]  # 画布，模型设置 可在function/subject 调整
          
          
food_num=5
color_output_name='1684178096'
color_style=0
K_Means= 30  # K-Means算法分成K类
init_method= 'random'
random_state= 88  # 艺术家风格分箱颜色数
color_distance= 300  # 艺术家风格颜色差异距离检查
chooesId=1
train=False

food_name='测试09'
food_price=900
food_notes='测试09'


starts=900
end=5900
space=300
add=0

# 是否显示
isShow=True

app_start = 0