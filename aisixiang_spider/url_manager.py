# coding=utf-8

# url管理器
import re
from urllib import parse, request

from bs4 import BeautifulSoup


class UrlManager(object):
    def __init__(self):
        # self.new_urls = {'http://www.aisixiang.com/data/106033.html', 'http://www.aisixiang.com/data/105997.html', 'http://www.aisixiang.com/data/106373.html', 'http://www.aisixiang.com/data/106471.html', 'http://www.aisixiang.com/data/106272.html', 'http://www.aisixiang.com/data/106265.html', 'http://www.aisixiang.com/data/106515.html', 'http://www.aisixiang.com/data/106417.html', 'http://www.aisixiang.com/data/105960.html', 'http://www.aisixiang.com/data/105828.html', 'http://www.aisixiang.com/data/106267.html', 'http://www.aisixiang.com/data/79807.html', 'http://www.aisixiang.com/data/105562.html', 'http://www.aisixiang.com/data/106159.html', 'http://www.aisixiang.com/data/106302.html', 'http://www.aisixiang.com/data/106353.html', 'http://www.aisixiang.com/data/106393.html', 'http://www.aisixiang.com/data/106437.html', 'http://www.aisixiang.com/data/106522.html', 'http://www.aisixiang.com/data/106372.html', 'http://www.aisixiang.com/data/106545.html'}

        self.new_urls = set()
        self.old_urls = set()

    # 添加新url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            header = {'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
                      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
            req = request.Request(url, data=None, headers=header)
            response = request.urlopen(req, timeout=10000)
            html_cont = response.read()
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
            links = soup.find_all('a', href=re.compile("/data/\d+\.html"))
            for link in links:
                new_url = link['href']
                new_full_url = parse.urljoin(url, new_url)
                self.new_urls.add(new_full_url)
            """"""
            # self.new_urls.add(url)
            print(['url_mgr', self.new_urls])

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
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
