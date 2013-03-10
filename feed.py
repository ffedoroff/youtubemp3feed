#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json, glob
from pprint import pprint
files = sorted(glob.glob("json/Бизнес-секреты/*.json"))


out = """
<html>
<head><head>
<body>
<ul>
"""

for file in files:
	#print file
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()
	out += "<li>"
	out += '<img src="'+data["thumbnail"]+'" />'
	out += data["number_in_playlist"].zfill(3)+" "+data["short_title"]
	out += "</li>"

out += """
</ul>
</body>
</html>
"""

f = open("res.html", 'w')
f.write(out.encode("utf-8"))
f.close()