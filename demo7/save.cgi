#!/usr/bin/python
import cgi
import sys

import psycopg2

print('Content-type: text/html\n')
conn = psycopg2.connect('user=foo password=bar dbname=baz')
curs = conn.cursor()
form = cgi.FieldStorage()
sender = form.getvalue('sender')
subject = form.getvalue('subject')
text = form.getvalue('text')
reply_to = form.getvalue('reply_to')
if not (sender and subject and text):
    print('Please supply sender,subject,and text')
    sys.exit()
if reply_to is not None:
    query = ("""
    INSERT INTO message(reply_to,sender,subject,text)
    VALUES (%s,'%s','%s','%s')
    """, (int(reply_to), sender, subject, text))
else:
    query = ("""
    INSERT INTO message(sender,subject,text)
    VALUES ('%s','%s','%s')
    """, (sender, subject, text))
curs.execute(*query)
conn.commit()
print("""
<html>
	<head>
		<title>Message Saved</title>
	</head>
	<body>
		<h1>
			Message Saved
		</h1>
		<hr />
		<a href="main.cgi">Back to the main page</a>
	</body>
</html>
""")
