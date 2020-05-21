# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:41
# @Author  : vothin
# @File    : global_path.py

# ****************************************************************

import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)

excel_path = os.path.join(BIR, r'data\食物成分热量表.xls')
log_path = os.path.join(BIR, r'log\log.log')
url_path = os.path.join(BIR, r'config\url.yaml')
