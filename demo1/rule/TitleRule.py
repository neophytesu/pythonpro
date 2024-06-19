import HeadingRule


class HeadlineRule(HeadingRule):
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)
