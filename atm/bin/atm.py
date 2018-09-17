#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 0019 下午 18:02
# @Author  : xiaoyafei
# @Site    : 
# @File    : atm.py
# @Software: PyCharm

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':
    main.run()