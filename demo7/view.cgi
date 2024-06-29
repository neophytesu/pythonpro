#!/usr/bin/python
import cgi
import sys

import psycopg2

print('Content-type: text/html\n')
conn = psycopg2.connect('user=foo password=bar dbname=baz')
curs = conn.cursor()
form = cgi.FieldStorage()
id = form.getvalue('id')
print("""
<html>
    <head>
        <title>View Message</title>
    </head>
    <body>
		<h1>
			View Message
		</h1>
""")
try:
    id = int(id)
except:
    print('Invalid message ID')
    sys.exit()
curs.execute('SELECT * FROM message WHERE id=%s', (format(id),))
rows = curs.dictfetchall()
if not rows:
    print('Unknow message ID')
    sys.exit()
row = rows[0]
print("""
<p>
			<b>Subject:</b>{subject}<br />
			<b>Sender:</b>{sender}<br />
		<pre>{text}</pre>
		<hr />
		<a href='main.cgi'>Back to the main page</a>
		<a href='edit.cgi?reply_to={id}'>Reply</a>
		</p>
	</body>
</html>
""".format(row))
