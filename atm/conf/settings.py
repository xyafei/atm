#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 18:05
# @Author  : xiaoyafei
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DATABASE = {
    'engine': 'file_storage',
    'name':'account',
    'path':'%s\db\\' % BASE_DIR
}



TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0.03},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}
