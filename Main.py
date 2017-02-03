#!/usr/bin/env python3
# coding:utf-8
from channel_ganji import channel_list
from mpage_ganji import get_links, get_info, ganji_url_list, ganji_info
from multiprocessing import Pool
import time

db_urls = [item['url'] for item in ganji_url_list.find()]
index_urls = [item['url'] for item in ganji_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y


def get_all_links(channel):
	for i in range(1, 115):
		get_links(channel, i)


# if __name__ == '__main__':
# 	pool=Pool()
# 	pool.map(get_all_links,channel_list.split())
# 	pool.close()
# 	pool.join()


# ganji_info表显示信息
if __name__ == '__main__':
	pool = Pool()
	pool.map(get_info, rest_of_urls)
	pool.close()
	pool.join()
