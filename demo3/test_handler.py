from xml.sax import parse
from xml.sax.handler import ContentHandler


class TestHandler(ContentHandler):

    def startElement(self, name, attrs):
        print(name, attrs.keys())


parse('website.xml', TestHandler())
