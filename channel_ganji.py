#!/usr/bin/env python3
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import time

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
	'Cookie': 'citydomain=sh; statistics_clientid=me; ganji_uuid=2534106406860724147966; ganji_xuuid=5233cbd7-4490-45ad-e6d1-a023c73262b0.1460299324358; __utmt=1; GANJISESSID=f929f545102d4d411b1c5cf983903f2b; lg=1; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A79612613894%7D; __utma=32156897.1973734604.1460299302.1460344835.1460383613.5; __utmb=32156897.3.10.1460383613; __utmc=32156897; __utmz=32156897.1460383613.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
	'Referer': 'http://sh.ganji.com/wu/'

}

start_url = 'http://sh.ganji.com/wu/'


def get_urls(url):
	wb_data = requests.get(start_url, headers=headers)
	soup = BeautifulSoup(wb_data.text, 'lxml')
	links = soup.select('div.main-pop  dl dt a')
	for link in links:
		page_url = 'http://sh.ganji.com' + link.get('href')
		print(page_url)


# get_urls(start_url)


channel_list = '''
	http://sh.ganji.com/shouji/
	http://sh.ganji.com/shoujihaoma/
	http://sh.ganji.com/shoujipeijian/
	http://sh.ganji.com/bijibendiannao/
	http://sh.ganji.com/taishidiannaozhengji/
	http://sh.ganji.com/diannaoyingjian/
	http://sh.ganji.com/wangluoshebei/
	http://sh.ganji.com/shumaxiangji/
	http://sh.ganji.com/youxiji/
	http://sh.ganji.com/xuniwupin/
	http://sh.ganji.com/jiaju/
	http://sh.ganji.com/jiadian/
	http://sh.ganji.com/zixingchemaimai/
	http://sh.ganji.com/rirongbaihuo/
	http://sh.ganji.com/yingyouyunfu/
	http://sh.ganji.com/fushixiaobaxuemao/
	http://sh.ganji.com/meironghuazhuang/
	http://sh.ganji.com/yundongqicai/
	http://sh.ganji.com/yueqi/
	http://sh.ganji.com/tushu/
	http://sh.ganji.com/bangongjiaju/
	http://sh.ganji.com/wujingongju/
	http://sh.ganji.com/nongyongpin/
	http://sh.ganji.com/xianzhilipin/
	http://sh.ganji.com/shoucangpin/
	http://sh.ganji.com/baojianpin/
	http://sh.ganji.com/laonianyongpin/
	http://sh.ganji.com/gou/
	http://sh.ganji.com/qitaxiaochong/
	http://sh.ganji.com/xiaofeika/
	http://sh.ganji.com/menpiao/
'''
