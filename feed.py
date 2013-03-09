#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json
from pprint import pprint
json_data=open('json/Бизнес-секреты/Filip Engelbert.json')

data = json.load(json_data)
#pprint(data)
print data["id"]
json_data.close()