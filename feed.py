#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json
from pprint import pprint
files = sorted(glob.glob("json/Бизнес-секреты/*.json"))
for file in files:
	print file
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()