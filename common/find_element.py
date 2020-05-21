# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 18:12
# @Author  : vothin
# @File    : find_element.py

# ****************************************************************


from base.base import Base

class FindElement(Base):

    def find(self, *loc):
        return self.driver.find_element(loc)

    def finds(self, *loc):
        return self.driver.find_elements(loc)

    def find_id(self, *loc):
        return self.driver.find_element_by_id(loc)

    def finds_ids(self, *loc):
        return self.driver.find_elements_by_id(loc)

    def find_class(self, *loc):
        return self.driver.find_element_by_class_name(loc)

    def finds_class(self, *loc):
        return self.driver.find_elements_by_class_name(loc)

    def find_xpath(self, *loc):
        return self.driver.find_element_by_xpath(loc)

    def finds_xpath(self, *loc):
        return self.driver.find_elements_by_xpath(loc)

    def find_name(self, *loc):
        return self.driver.find_element_by_name(loc)

    def finds_name(self, *loc):
        return self.driver.find_elements_by_name(loc)

    def find_tag_name(self, *loc):
        return self.driver.find_element_by_tag_name(loc)

    def finds_tag_name(self, *loc):
        return self.driver.find_elements_by_tag_name(loc)
