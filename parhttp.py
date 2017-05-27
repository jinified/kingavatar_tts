#!/usr/bin/env python
import sys
import urllib2
import requests
import codecs

from multiprocessing import Process, Pool
from bs4 import BeautifulSoup

PREFIX = "http://quanzhigaoshou.booksrc.net/"

def http_get(url):
    r = requests.get(url[0])
    data = BeautifulSoup(r.content, 'html.parser')
    content = data.find(name='div', attrs={'class': 'bookcontent'})
    if content:
        with codecs.open('out/{}.txt'.format(url[1]), 'w', encoding='utf8') as f:
            f.write(content.get_text())
        return url[1]

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("At least one index is needed")
        exit()
    elif len(sys.argv) < 3:
        urls = [('{}{}.html'.format(PREFIX, sys.argv[1]), sys.argv[1])]
    else:
        urls = [('{}{}.html'.format(PREFIX, i), i) for i in range(sys.argv[1], sys.argv[2] + 1)]

    # Use maximum number of processes
    pool = Pool()

    results = []
    results = pool.map(http_get, urls)

    pool.close()
    pool.join()
