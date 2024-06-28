#!/usr/bin/env python
import cgi
import sys
from hashlib import sha1
from os.path import abspath
from shlex import join

print("Content-type:text/html")
BASE_DIR = abspath("data")
form = cgi.FieldStorage()
text = form.getvalue("text")
filename = form.getvalue("filename")
password = form.getvalue("password")
if not (filename and password and text):
    print("Invalid parameters")
    sys.exit()
if sha1(password.encode()).hexdigest() != "b0b0c0d0":
    print("Invalid password")
    sys.exit()
f = open(join(BASE_DIR, filename), 'w')
f.write(text)
f.close()
print('The file has been saved')
