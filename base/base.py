# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:44
# @Author  : vothin
# @File    : base.py

# ****************************************************************

from selenium import webdriver
from common.record_log import logs

class Base():

    # 启动浏览器
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        logs.info('启动浏览器')


    # 关闭浏览器
    def driverClose(self):
        self.driver.close()
        logs.info('关闭浏览器')











