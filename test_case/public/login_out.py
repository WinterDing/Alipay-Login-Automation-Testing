#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com

#login
def login(self, username, password):
    driver = self.driver
    #点击登录
    driver.find_element_by_partial_link_text('登录').click()
    #选择帐密登录
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[2]').click()
    driver.find_element_by_id('J-input-user').clear()
    driver.find_element_by_id('J-input-user').send_keys(username)
    driver.find_element_by_id('password_rsainput').clear()
    driver.find_element_by_id('password_rsainput').send_keys(password)
    driver.find_element_by_id('J-login-btn').click()

#logout
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text('退出').click()