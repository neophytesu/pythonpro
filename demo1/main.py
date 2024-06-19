import sys

from demo1.parse.BasicTextParser import BasicTextParser
from demo1.resolve.HTMLRenderer import HTMLRenderer

# 自动添加标签
handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)
