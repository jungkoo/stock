# -*- coding: utf-8 -*-
import simplejson as json
import urllib2, urllib
import bs4
from bs4 import BeautifulSoup


def get_html(link, cp949=False, chunk_size=None, params=None):
    req = urllib2.Request(link)
    req.add_header('User-Agent', 'Mozilla/1.0 beta')
    req.add_header('Cookie', 'pcid=1403512471525')  #  auction check data.
    if params:
        params = urllib.urlencode(params)

    handle = urllib2.urlopen(req, data=params, timeout=5)
    if chunk_size:
        data = handle.read(chunk_size)
    else:
        data = handle.read()
    data = data.decode('cp949', 'ignore') if cp949 else data
    handle.close()
    return data


def get_json(link, cp949=False, chunk_size=None, params=None):
    html = get_html(link, cp949, chunk_size, params)
    return json.loads(html)


def base_dict():
    rv = dict()
    rv['code'] = '' # 코드
    rv['name'] = '' # 종목명
    rv['date'] = '' # 날짜
    rv['price_max'] = 0 # 고가
    rv['price_min'] = 0 # 저가
    rv['price_start'] = 0 # 시가
    rv['price_end'] = 0 # 종가
    rv['trade_cnt'] = 0 # 거래량
    return rv

if __name__ == '__main__':
    print get_json('http://m.stock.naver.com/api/item/getPriceDayList.nhn?code=009830&pageSize=20&page=1')