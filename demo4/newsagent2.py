import re
import textwrap
from nntplib import NNTP, decode_header
from urllib.request import urlopen


class NewsAgent:
    def __init__(self):
        self.sources = []
        self.destinations = []

    def add_source(self, source):
        self.sources.append(source)

    def add_destination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        items = []
        for source in self.sources:
            items.extend(source.get_items())
        for dest in self.destinations:
            dest.receive_items(items)


class NewsItem:
    def __init__(self, title, body):
        self.title = title
        self.body = body


class NNTPSource:
    def __init__(self, servername, group, howmany):
        self.servername = servername
        self.group = group
        self.howmany = howmany

    def get_items(self):
        server = NNTP(self.servername)
        resp, count, first, last, name = server.group(self.group)
        start = last - self.howmany + 1
        resp, overviews = server.over((start, last))
        for id, over in overviews:
            title = decode_header(over['subject'])
            resp, info = server.body(id)
            body = '\n'.join(line.decode('latin') for line in info.lines) + '\n\n'
            yield NewsItem(title, body)
        server.quit()


class SimpleWebSource:
    def __init__(self, url, title_pattern, body_pattern, encoding='utf-8'):
        self.url = url
        self.title_pattern = re.compile(title_pattern)
        self.body_pattern = re.compile(body_pattern)
        self.encoding = encoding

    def get_items(self):
        text = urlopen(self.url).read().decode(self.encoding)
        titles = self.title_pattern.findall(text)
        bodies = self.body_pattern.findall(text)
        for title, body in zip(titles, bodies):
            yield NewsItem(title, textwrap.fill(body) + '\n')


class PlainDestination:
    def receive_items(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)


class HTMLDestination:
    def __init__(self, filename):
        self.filename = filename

    def receive_items(self, items):
        out = open(self.filename, 'w')
        print("""
        <html>
            <head>
                <title>Today's News</title>
            </head>
            <body>
            <h1>Today's News</h1>
        """, file=out)
        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print(' <li><a href="#{}">{}</a></li>'.format(id, item.title), file=out)
        print('</ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print('<a name="{}"><h2>{}</h2></a>'.format(id, item.title), file=out)
            print('<pre>{}</pre>'.format(item.body), file=out)
        print("""
            </body>
            </html>
        """, file=out)


def runDefaultSetup():
    agent = NewsAgent()
    reuters_url = 'http://www.reuters.com/news/world'
    reuters_title = r'<h2><a href="[^"]*"\s*>(.*?)</a>'
    reuters_body = r'</h2><p>(.*?)</p>'
    reuters = SimpleWebSource(reuters_url, reuters_title, reuters_body)
    agent.add_source(reuters)
    clpa_server = 'news.foo.bar'
    clpa_server = 'news.ntnu.no'
    clpa_group = 'com.lang.python.announce'
    clpa_howmany = 10
    clpa = NNTPSource(clpa_server, clpa_group, clpa_howmany)
    agent.add_source(clpa)
    agent.add_destination(PlainDestination())
    agent.add_destination(HTMLDestination('news.html'))
    agent.distribute()


if __name__ == '__main__':
    runDefaultSetup()
