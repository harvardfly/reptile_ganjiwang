#!/usr/bin/env python3
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganjiwang = client['ganjiwang']
ganji_url_list = ganjiwang['ganji_url_list']
ganji_info = ganjiwang['ganji_info']

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
	'Cookie': 'citydomain=sh; statistics_clientid=me; ganji_uuid=2534106406860724147966; ganji_xuuid=5233cbd7-4490-45ad-e6d1-a023c73262b0.1460299324358; __utmt=1; GANJISESSID=f929f545102d4d411b1c5cf983903f2b; lg=1; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A79612613894%7D; __utma=32156897.1973734604.1460299302.1460344835.1460383613.5; __utmb=32156897.3.10.1460383613; __utmc=32156897; __utmz=32156897.1460383613.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
	'Referer': 'http://sh.ganji.com/wu/'

}


def get_links(channel, pages, whosells='o'):
	# http://sh.ganji.com/shouji/o3个人
	# http://sh.ganji.com/shouji/a2o3 商家
	list_links = '{}{}{}/'.format(channel, whosells, str(pages))
	try:
		wb_data = requests.get(list_links, headers=headers)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		# if soup.find('dt','a '):
		for link in soup.select('dl.list-bigpic.clearfix dt a'):
			item_link = link.get('href')
			# if 'zhuanzhuan' not in link.get('href'):
			ganji_url_list.insert_one({'url': item_link})
	except AttributeError:
		pass
	except IndexError:
		pass
	except requests.exceptions.ConnectionError:
		pass
	except requests.exceptions.ChunkedEncodingError:
		pass


	# print(item_link)
	# else:
	# 	# 最后一页了
	# 	pass


def get_info(url):
	try:
		wb_data = requests.get(url, headers=headers)
		if wb_data.status_code == 404:
			pass
		else:
			soup = BeautifulSoup(wb_data.text, 'lxml')
			# titles=list(map(lambda x:x.text.strip(),soup.select('div.col-cont.title-box > h1')))
			data = {
				'title': soup.title.text.strip(),
				'price': soup.select('i.f22.fc-orange.f-type')[0].text,
				'area': list(map(lambda x: x.text.strip(), soup.select('ul.det-infor li:nth-of-type(3) a')[1:])),
				'fdate': soup.select('i.pr-5')[0].text.strip()[:-3],
				'cates': list(map(lambda x: x.text, soup.select('div.crumbs.routes.clearfix a'))),
				# 'look':soup.select('ul.second-det-infor.clearfix li') if soup.find_all('ul', 'second-det-infor.clearfix') else None,
				'url': url
			}
			ganji_info.insert_one(data)
			print(data)
	except AttributeError:
		pass
	except IndexError:
		pass
	except requests.exceptions.ConnectionError:
		pass
	except requests.exceptions.ChunkedEncodingError:
		pass

	# print(data)

# get_info('http://sh.ganji.com/ershoubijibendiannao/2035818304x.htm')
