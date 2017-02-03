#!/usr/bin/env python3
# coding:utf-8
import time
from mpage_ganji import ganji_url_list, ganji_info

# url_list 表



while True:
	print(u'ganji_url_list表数据条数：' + str(ganji_url_list.find().count()))
	print(u'ganji_info表数据条数：' + str(ganji_info.find().count()))
	time.sleep(2)
# 每隔2秒统计一次url_list里面的数据条数
