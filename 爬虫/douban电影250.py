#!/usr/bin/env python
#encoding = utf-8

import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def download_page(url):
    return requests.get(url).content

def parse_html(html):

    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})

    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class':'hd'})
        movie_name = detail.find('span', attrs={'class':'title'}).getText()
        movie_name_list.append(movie_name)

    next_page  = soup.find('span', attrs={'class':'next'}).find('a')

    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']

    return movie_name_list,None

def main():
    url = DOWNLOAD_URL

    with codecs.open('movies','wb',encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)

            fp.write(u'{movies}'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    main()


