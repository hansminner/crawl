# coding=utf-8

# url管理器
import re
from urllib import parse, request

from bs4 import BeautifulSoup


class UrlManager(object):
    def __init__(self):

        self.new_urls = set()
        self.old_urls = set()

    # 添加新url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            header = {
                'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_79f928fc7941d32d644966add293b492=1508725997,1508807317,1508832180,1508832304;'
                          ' Hm_lpvt_79f928fc7941d32d644966add293b492=1508835195',
                'Host': 'www.aisixiang.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/55.0.2883.87 Safari/537.36'
            }
            req = request.Request(url, data=None, headers=header)

            try:
                response = request.urlopen(req, timeout=10000)
            except ZeroDivisionError:
                print('failded')

            html_cont = response.read()
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
            links = soup.find_all('a', href=re.compile("/data/\d+\.html"))
            for link in links:
                new_url = link['href']
                new_full_url = parse.urljoin(url, new_url)
                self.new_urls.add(new_full_url)
            """"""
            # self.new_urls.add(url)
            # print(['url_mgr', self.new_urls])

    # 添加批量
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断时候新url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取新的url
    def get_new_url(self):
        # dui
        new_url = self.new_urls.pop()
        # dui
        self.old_urls.add(new_url)
        return new_url
