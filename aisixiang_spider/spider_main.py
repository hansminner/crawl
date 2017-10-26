# coding=utf-8

# alt+enter 快速创建方法和类 self指的是描述符类的实例
import time

from aisixiang_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 给C + + / Java / C\# 程序员的注释Python中的self等价于C++中的self指针和Java、C#中的this参考。

    def __init__(self):
        # url调度器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 记录当前爬去的第几个url
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            # 异常处理
            try:
                new_url = self.urls.get_new_url()
                # 下载好的页面数据
                # new_url 不对
                # print(new_url)
                html_cont = self.downloader.download(new_url)
                print(html_cont),
                return
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                """
                if count == 83:
                    break

                count = count + 1
                """

            except ZeroDivisionError:
                print('craw failed')

        self.outputer.out_html()


if __name__ == "__main__":
    # setting url
    root_url = "http://www.aisixiang.com/thinktank/yangguangbin.html"
    # create SpiderMain
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
