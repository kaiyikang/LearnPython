#!/usr/bin/env python
# encoding=utf-8

import codecs
import requests

from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://www.douban.com/people/Oceannagirl/notes'

def download_page(url):
    data = requests.get(url).content
    return data

def parse_html(html):

    soup = BeautifulSoup(html)
    title_list_soup = soup.find('div',attrs={'class':'article'})

    article_title_list = []

    for title_div in title_list_soup.find_all('div',attrs={'class':'note-container'}):
        article_title = title_div.find('h3').getText()
        article_title_list.append(article_title)

    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return article_title_list, DOWNLOAD_URL + next_page['href']

    return article_title_list , None



def main():
    url = DOWNLOAD_URL

    with codecs.open('title','wb',encoding = 'utf-8') as fp:
        while url:#最后一页没有url就不用输出了
            html = download_page(url)
            title, url = parse_html(html)
            fp.write(u'{title}\n'.format(title = '\n'.join(title)))






if __name__ =='__main__':
    main()


