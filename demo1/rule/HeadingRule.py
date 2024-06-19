import Rule


class HeadingRule(Rule):
    type = 'heding'

    def condition(self, block):
        return '\n' not in block and len(block) <= 70 and not block[-1] == ':'


def condition(self, block):
    return None