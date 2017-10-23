# coding=utf-8

import re
from bs4 import BeautifulSoup
from urllib import parse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 解析url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # <a href="/data/95514.html" target="_blank">丰裕中的思想贫困——兼论中国教育—科学管理体制的问题与出路</a>
        # links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        links = soup.find_all('a', href=re.compile("/data/\d+\.html"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    # 解析数据
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        title_node = soup.find('h3')

        # title_node = soup.find('div', class_="show_text").find("h3")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', id="content2")
        res_data['summary'] = summary_node.get_text()
        return res_data

