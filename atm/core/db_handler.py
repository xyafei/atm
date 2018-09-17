#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 20:25
# @Author  : xiaoyafei
# @Site    : 
# @File    : db_handler.py
# @Software: PyCharm

import os
import json
from conf import settings

def file_db_handle():

    return file_execute

def db_handler():
    '''连接数据库'''
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle()
    elif conn_params['engine'] == 'sql':
        pass

def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE
    db_path = '%s%s'%(conn_params['path'], conn_params['name'])

    sql_list = sql.split("where")

    if sql_list[0].startswith('select') and len(sql_list)>1:
        column,val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = r"%s\%s.json"%(db_path,val)
            print(db_path)
            print(val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file,'r') as f:
                    account_file = json.load(f)
                    return account_file
            else:
                exit("\033[31;1m用户 [%s] 不存在\033[0m" % val)

    elif sql_list[0].startswith("update") and len(sql_list)> 1:
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            #print(account_file)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                return True