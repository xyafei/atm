#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 17:58
# @Author  : xiaoyafei
# @Site    : 
# @File    : account_sample.py
# @Software: PyCharm

import json

sample = {
    'id':'xiaoming',
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_data':'2018-05-19',
    'expire_data':'2023-05-19',
    'pay_day':22,
    'status':0
}
f = open('xiaoming.json','w')
json.dump(sample,f)