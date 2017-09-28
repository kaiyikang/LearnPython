import requests
class HtmlDownLoader(object):

    def download(self,url):
        if url is None:
            return None

        #直接请求
        r = requests.get(url)
        r.encoding = 'utf-8'
        if r.status_code != 200:
            return None
        else:
            return r.text