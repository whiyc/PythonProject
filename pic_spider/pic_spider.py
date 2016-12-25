#!/usr/bin/env python
# encoding: utf-8
import urllib
import os
from urllib import request
from bs4 import BeautifulSoup


def load_pic(url, pager):
    ''' 抓取图片
    http://imgsrc.baidu.com/forum/w%3D580/sign=24afd400b112c8fcb4f3f6c5cc0392b4/4be95134970a304e733b06dad9c8a786c8175cef.jpg
    '''

    mRequest = creat_request(url)
    html = request.urlopen(mRequest)
    obj = BeautifulSoup(html)
    imgUrls = obj.find_all('img', class_='BDE_Image')

    dir_pic = r'F:\ooxx\pager%s' % pager
    flag = os.path.exists(dir_pic)
    if not flag:
        os.makedirs(dir_pic)
    index = 0

    for imgUrl in imgUrls:
        pic_url = imgUrl['src']
        isPic = pic_url.find('imgsrc.baidu.com')
        if not isPic == -1:
            dir_name = dir_pic + r'\%d.jpg' % index
            request.urlretrieve(pic_url, dir_name)

        index += 1


def creat_request(url):
    ''' 创建 request 对象'''
    hdr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }

    mRequest = request.Request(url, headers=hdr)

    return mRequest


def getContent(url):
    '''获取信息'''

    mRequest = creat_request(url)
    html = request.urlopen(mRequest)
    obj = BeautifulSoup(html)
    last_pager = obj.find('a', text='尾页')
    pager = last_pager['href']
    split = pager.split('=')
    n = split[-1]
    index = int(n) + 1
    # load_pic('http://tieba.baidu.com/p/4614362147', 1)

    for x in range(1, index):
        image_url = url + r'?pn=%d' % x
        load_pic(image_url, x)


info = getContent('http://tieba.baidu.com/p/4614362147')
