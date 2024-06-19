class Rule:
    def __init__(self):
        self.type = None

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
