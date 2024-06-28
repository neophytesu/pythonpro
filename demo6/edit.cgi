#!/usr/bin/env python
import cgi
import sys
from os.path import abspath
from shlex import join

print("Content-type:text/html")
BASE_DIR = abspath('data')
form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print('Please enter a file name')
    sys.exit()
text = open(join(BASE_DIR, filename)).read()
print("""
<html>
	<head>
		<title>Editing...</title>
	</head>
	<body>
		<form action="save.cgi" method="post">
			<b>File:</b>{}<br />
			<input type="hidden" value="{}" name="filename" />
			<b>Password</b><br />
			<input name='password' type="password" /><br />
			<b>Text:</b><br />
			<textarea rows="10" cols="20" name="text">{}</textarea><br />
			<input type="submit" value="Save"/>
		</form>
	</body>
</html>
""".format(filename, filename, text))
