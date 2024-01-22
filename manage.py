# -*- coding: utf-8 -*-

"""
@author: wangqi
@software: PyCharm
@file: manage.py
@time: 2023/3/31 22:43
"""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host="0.0.0.0", port=8080)
    # import requests
    # from bs4 import BeautifulSoup
    # import os
    # import sys
    #
    # for i in range(1, 28):
    #     url = "https://docs.oracle.com/javase/8/docs/api/"
    #     r = requests.get(url).content
    #     soup = BeautifulSoup(r).select('dt')
    #     for n, x in enumerate(soup):
    #         path = x.a.attrs['href']
    #         if '#' not in path:
    #             file = path[3:]
    #             url = "https://blog.fondme.cn/apidoc/jdk-1.8-google/index-files/" + path
    #             r = requests.get(url).content
    #             sou = BeautifulSoup(r).select('.header,.contentContainer')
    #             d = os.path.dirname(file)
    #             if not os.path.exists(d):
    #                 os.makedirs(d)
    #             with open(file, 'w') as f:
    #                 f.write(str(sou[0]) + str(sou[1]))
    #         sys.stdout.write('\r[%d/%d/%d] %s done!' % (n, len(soup), i, file))