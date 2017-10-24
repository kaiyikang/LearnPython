import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownLoader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, root_url):
        count = 1

        # 1. 将root url 输入进url管理器
        self.urls.add_new_url(root_url)
        # 2. 启动爬虫的循环
        #   当有待爬取的url地址
        while self.urls.has_new_url:

            # 1. 获取
            new_url = self.urls.get_new_url()

            # 2.启动下载器，下载页面，存储在count中
            html_count = self.downloader.download(new_url)

            # 3.调用解析器，得到新的url列表 和 相应的数据
            new_urls, new_data = self.parser.parse(new_url, html_count)

            # 4. 新的url 进入管理器
            self.urls.add_new_urls(new_urls)

            # 5.收集数据
            self.outputer.collect_data(new_data)

            if count == 30:
                break
            count += 1

        # 将收集好的数据输出
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    # 建立类的实例
    obj_spider = SpiderMain()
    # 导入root url
    obj_spider.craw(root_url)
