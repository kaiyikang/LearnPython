import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser (object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        print(html_cont)
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取新的urls
    def _get_new_urls (self, page_url, soup):

        new_urls = set() # /item/123.html
        links = soup.find_all('a',href=re.compile(r'/item'))

        for link in links:
            new_url = link['href']
            # 让 new_url 以 page_url 为模板拼接成一个全新的 url
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)

            # page_url  = https://baike.baidu.com/item/Python
            # new_url = /item/HTML
            # 在经过了urljoin的拼接之后
            # 得到https://baike.baidu.com/item/HTML
        return new_urls

    # 获取新的数据
    def _get_new_data (self, page_url, soup):

        res_data = {}


        res_data['url'] = page_url

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        if title_node is None: #如果title node 没有，直接跳过
            res_data['title'] = ''
            res_data['summary'] = ''
            return res_data

        res_data['title'] = title_node.get_text()


        summary_node = soup.find('div', class_='Lemma-summary')
        if summary_node is None:
            res_data['summary'] = ''
        else:
            res_data['summary'] = summary_node.get_text()


        return res_data
        
        # 这个方法解析出两个数据：新的url列表 和 数据
