import Rule


class ListItemRule(Rule):
    type = 'listitem'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


def condition(self, block):
    return block[0] == '-'
