class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    #收集数据
    def collect_data(self,data):
        #如果data啥都没有
        if data is None:
            return

        #否则，把data加入到data中去
        self.datas.append(data)

    #将数据变成html
    def output_html(self):
        #新建一个文件
        with open('output.html','w',encoding='utf-8') as fout:

            fout.write("<meta charset=\'utf-8\'>")
            fout.write("<html>")
            fout.write("<body>")
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
