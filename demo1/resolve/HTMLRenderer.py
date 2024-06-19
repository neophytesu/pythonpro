def start_paragraph():
    print('<p>')


def end_paragraph():
    print('</p>')


def sub_emphasis(match):
    return '<em>%s</em>' % match.group(1)


def feed(data):
    print(data)


def start_document():
    print('<html><head><title>...</title></head><body>')


def end_document():
    print('</body></html>')


def start_heading():
    print('<h2>')


def end_heading():
    print('</h2>')


def start_list():
    print('<ul>')


def end_list():
    print('</ul>')


def start_listitem():
    print('<li>')


def end_listitem():
    print('</li>')


def start_title():
    print('<h1>')


def end_title():
    print('</h1>')


def sub_url(match):
    return '<a href="%s">%s</a>' % (match.group(1), match.group(1))


def sub_mail(match):
    return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))


class HTMLRenderer:
    pass
