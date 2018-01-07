#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com

import unittest
import HTMLTestRunner
import time

def createSuite(test_dir, pattern):
    return unittest.defaultTestLoader.discover(test_dir, pattern)

if __name__ == '__main__':
    #test cases directory
    test_dir = r'C:\Users\z218680\Desktop\Python\alipay_test\test_case'
    pattern = r'test*.py'
    #test report file
    current_time = time.strftime("%Y%m%d_%H%M%S")
    report_file = r'C:\Users\z218680\Desktop\Python\alipay_test\report\result_{now}.html'.format(now=current_time)
    # open report file
    fp = open(report_file, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = 'Alipay Login Testing',
            description = 'Testing result: '
        )
    #start to run testing
    runner.run(createSuite(test_dir, pattern))
    fp.close()