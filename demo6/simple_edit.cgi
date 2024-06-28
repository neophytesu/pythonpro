#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
text = form.getvalue('text', open('simple_edit.dat').read())
f = open('simple_edit.dat', 'w')
f.write(text)
f.close()
print("""
Content-type:text/html
<html>
	<head>
		<meta charset="utf-8">
		<title>Simple Edit</title>
	</head>
	<body>
		<form action="simple_edi_cgi" method="post">
			<textarea rows="10" cols="20" name="text">{}</textarea><br />
			<input type="submit" />
		</form>
	</body>
</html>
""".format(text))
