#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 18:47
# @Author  : xiaoyafei
# @Site    : 
# @File    : shopping_mall.py
# @Software: PyCharm

import json
import os

def product():

    shopping_cart = []  # 购物车

    product_list = [
        ['Iphone7 Plus', 6500],
        ['Iphone8 ', 8200],
        ['MacBook Pro', 12000],
        ['Python Book', 99],
        ['Coffee', 33],
        ['Bike', 666],
        ['pen', 2]
    ]
    while True:
        print('----------欢迎光临本商城----------')
        print('%s\t\t%s\t\t%s'%('编号','商品','价格'))
        for index,k in enumerate(product_list):
            print("%s.\t%s\t%s" % (index, k[0], k[1]))

        choice = input('>>请输入你要购买的商品编号    exit退出:<<').strip()
        if len(choice) == 0:
            print('>>您没有输入任何商品<<')
            continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(product_list) and choice > 0:
                item = product_list[choice]
                shopping_cart.append(item)
                print('添加 \033[32;1m%s\033[0m 到购物车车'%(item[0]))
            else:
                print('没有本商品')
        elif choice == 'exit':
            print('您的购物车列表：')
            for i in shopping_cart:
                print(i)
            # 以下是付款操作

        # auth_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前工作目录
        # auth_file2 = '\db\%s.json'% account  # 自定义的目录
        # auth_file3 = auth_file+auth_file2
        # f = open(auth_file3,'r')
        # data = json.load(f)






