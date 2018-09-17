#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 18:11
# @Author  : xiaoyafei
# @Site    : 
# @File    : auth.py
# @Software: PyCharm

import json
import os
import time
from core import shopping_mall
from core import db_handler
# from conf import settings

def acc_auth2(account,password):
    db_api = db_handler.db_handler()
    data = db_api('select * from accounts where account=%s'%account)
    print(data)  # 文件
    if data['password'] == password:
        # exp_time_stamp = time.mktime(time.strptime(data['expire_data'], "%Y-%m-%d"))
        # if time.time() > exp_time_stamp:
        #     print('请去申请一张新的卡片...')
        # else:
            return data
    else:
        print('用户名或密码不正确')



def acc_auth(user_data):

    while user_data['is_authenticated']  is not True:
        account = input('请输入用户名：')
        password = input('请输入密码：')

        auth = acc_auth2(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account

            return auth








