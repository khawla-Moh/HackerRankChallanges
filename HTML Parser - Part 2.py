from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:     
            print('>>> single-line Comment')
        print(comment)

    def handle_data(self, data):
        if '\n' in data :return
        print('>>> data')
        print(data)


NumberOfLine=input()
html=''
for _ in range (int(NumberOfLine)):
    html +=input().strip()
    html +='\n'
    
    
parser=MyHTMLParser()
parser.feed(html)
parser.close()     