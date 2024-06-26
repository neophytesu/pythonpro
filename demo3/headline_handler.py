from xml.sax import parse
from xml.sax.handler import ContentHandler


class HeadHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        super().__init__()
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


headlines = []
parse('website.xml', HeadHandler(headlines))
print('The Following <h1> elements were found:')
for h in headlines:
    print(h)
