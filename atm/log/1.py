#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 22:45
# @Author  : xiaoyafei
# @Site    : 
# @File    : 1.py
# @Software: PyCharm


import logging  # 导入logging模块

# 1.创建logger
logger = logging.getLogger('web')  # 创建一个叫web的logger
# 1.1设置全局输出日志的等级
logger.setLevel(logging.DEBUG)  # 允许DEBUG及以上级别的日志输出

# 2.创建handler
# 2.1屏幕handler
screen = logging.StreamHandler()
# 2.2文件handler
file = logging.FileHandler('web.log')  # 日志都输出到web.log中

# 2.3设置输出到屏幕和文件的等级
# screen.setLevel(logging.INFO)
# file.setLevel(logging.WARNING)

# 3.创建formatter
# 3.1创建输出到屏幕的格式
screen_formatter = logging.Formatter('%(asctime)s -- %(lineno)s -- %(message)s')
# 3.2创建输出到文件的格式
file_formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')


# 4.绑定handler
screen.setFormatter(screen_formatter)
file.setFormatter(file_formatter)


# 5.绑定logger
logger.addHandler(screen)
logger.addHandler(file)

logger.debug('this is DEBUG ingo')
logger.info('this is INFO ingo')
logger.warning('this is WARNING ingo')
logger.error('this is error ingo')