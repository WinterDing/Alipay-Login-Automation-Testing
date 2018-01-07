#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com

from selenium import webdriver
import unittest, time
from test_case.public import login_out
import json


login_accounts_file = r'C:\Users\z218680\Desktop\Python\alipay_test\conf\login.json'

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = accounts['url']

    def test_usr_pwd_null(self):
        """用户名密码都为空"""
        driver = self.driver
        #open website
        driver.get(self.base_url)
        driver.maximize_window()
        #get username, password, prompt
        username = accounts['usr_pwd_null']['usr']
        password = accounts['usr_pwd_null']['pwd']
        prompt = accounts['usr_pwd_null']['msg']
        #login
        login_out.login(self, username, password)
        #get response prompt and assert
        text = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/fieldset/div[1]/span').text
        self.assertEqual(text, prompt)

    def test_pwd_null(self):
        """密码为空，用户名非空"""
        driver = self.driver
        #open website
        driver.get(self.base_url)
        driver.maximize_window()
        #get username, password, prompt
        username = accounts['pwd_null']['usr']
        password = accounts['pwd_null']['pwd']
        prompt = accounts['pwd_null']['msg']
        #login
        login_out.login(self, username, password)
        #get response prompt and assert
        text = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/fieldset/div[1]/span').text
        self.assertEqual(text, prompt)

    def test_usr_null(self):
        """用户名为空，密码非空"""
        driver = self.driver
        #open website
        driver.get(self.base_url)
        driver.maximize_window()
        #get username, password, prompt
        username = accounts['usr_null']['usr']
        password = accounts['usr_null']['pwd']
        prompt = accounts['usr_null']['msg']
        #login
        login_out.login(self, username, password)
        #get response prompt and assert
        text = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/fieldset/div[1]/span').text
        self.assertEqual(text, prompt)

    def test_usr_pwd_wrong(self):
        """用户名密码错误"""
        driver = self.driver
        #open website
        driver.get(self.base_url)
        driver.maximize_window()
        #get username, password, prompt
        username = accounts['usr_pwd_wrong']['usr']
        password = accounts['usr_pwd_wrong']['pwd']
        prompt = accounts['usr_pwd_wrong']['msg']
        #login
        login_out.login(self, username, password)
        #get response prompt and assert
        text = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/fieldset/div[1]/span').text
        self.assertIn(text, prompt)

    def tearDown(self):
        self.driver.quit()

def getLoginInfo(info_file):
    """load login file information and return"""
    with open(info_file, 'r', encoding='utf-8') as login_fp:
        accounts = json.load(login_fp)
    return accounts

accounts = getLoginInfo(login_accounts_file)