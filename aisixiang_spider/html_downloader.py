# coding=utf-8

from urllib import request

import time


class HtmlDownloader(object):
    # 下载器 new_url 要下载的url
    def download(self, new_url):
        if new_url is None:
            return None

        # print(['html_d', new_url])

        # time.sleep(5)

        response = request.urlopen(new_url)

        if response.getcode() != 200:
            return None
        return response.read()


