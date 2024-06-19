import Parser
from demo1.rule.ListItemRule import ListItemRule
from demo1.rule.ListRule import ListRule
from demo1.rule.ParagraphRule import ParagraphRule
from demo1.rule.TitleRule import HeadlineRule


class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(HeadlineRule())
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
