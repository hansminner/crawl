# coding=utf-8

from urllib import request


class HtmlDownloader(object):
    # 下载器 new_url 要下载的url
    def download(self, new_url):
        if new_url is None:
            return None

        response = request.urlopen(new_url)

        if response.getcode() != 200:
            return None
        return response.read()

"""
 def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
        """