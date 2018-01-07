Summary: Alipay login testint
Author:	Winter Ding
Date: 2018-01-07
Description:
	Using Webdriver, Unittest to do Alipay login testing, include 5 test cases:
	1) username and password are null
	2) username is null, password is not null
	3) password is null, username is not null
	4) wrong username and password
	5) correct username and password
	After test finish, create testing result report with html format
Run testing steps:
	1) run 'start_test.py' main file in directory "alipay_test"
	2) check report in "alipay_test\report"
Problems:
	when running test case 5), always get error message"登录失败，你可以尝试使用扫码登录或稍后重试。"
	Still need to figure it out
Todo:
	Send report out by emails 