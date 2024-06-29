#!/usr/bin/env python
# addmessage.py
import psycopg2 as psycopg2

conn = psycopg2.connect("user=foo password=bar dbname=baz")
curs = conn.cursor()
reply_to = input('Reply to:')
subject = input('Subject:')
sender = input('Sender:')
text = input('Text')
if reply_to:
    query = """
    INSERT INTO message(reply_to,sender,subject,text)
    VALUES ({},'{}','{}','{}')
    """.format(reply_to, sender, subject, text)
else:
    query = """
    INSERT INTO message(sender,subject,text)
    VALUES ('{}','{}','{}')
    """.format(sender, subject, text)
curs.execute(query)
conn.commit()
