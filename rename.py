#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re, glob, json, sys
from pprint import pprint

"""
# resave json file
files = sorted(glob.glob("json/Бизнес-секреты/*.json"))
for file in files:
	print file
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()

	#change data object here
	data["number_in_playlist"] = str(data["number_in_playlist"])
	data["raw_audio"] = u"Бизнес-секреты/"+data["number_in_playlist"].zfill(3)+" "+data["short_title"]+".m4a"
	#end of change data object

	res = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '), encoding="utf-8", sort_keys=True)
	f = open(file, 'w')
	f.write(res.encode("utf-8"))
	f.close()

	#print filename
# end resave json file
"""

"""
for line in src:
    #print line
    res = re.sub('(Бизнес-секреты)|(Business Secrets)|( - )|(\.json)|(\.mp4)|(\.info)|(\.)', r'', line)
    # print res
    res = string.split(res, '-')
    res = res[0]+".json"

    #print 'mv -i "'+line+'" "'+res+'"'
    #print ""




files = sorted(glob.glob("json/Бизнес-секреты/*.json"))
files_audio = sorted(glob.glob("audio/Бизнес-секреты/*.m4a"))

i=0
for file in files:
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()

	
	print 'mv -i "'+ files_audio[i].decode('utf-8') + u'" "audio/Бизнес-секреты/' + str(data["number_in_playlist"]).zfill(3)+" "+data["short_title"]+'.m4a"'

	i += 1
	#print str(i)+" "+file


for file in files:
	#print file
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()
	#print data["title"]
	short_title = re.sub(u'(Бизнес-секреты:\ )|(Business Secrets:\ )', r'', data["stitle"])
	data["short_title"] = short_title
	res = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '), encoding="utf-8", sort_keys=True)
	#res = res.replace('\\n','\\n\n')
	#print res
	
	filename = str(data["number_in_playlist"]).zfill(3)+" "+short_title+".json"
	f = open(u'json/Бизнес-секреты/'+filename, 'w')
	f.write(res.encode("utf-8"))
	f.close()
	print filename
	#sys.exit(0)
	#pprint(data)
	#print data["id"]
	#lineNumber = 1
	#for line in src:
		#if lineNumber > 1: continue
		#if data["id"] in line.decode("utf-8"):
			#print str(lineNumber)+" "+data["id"]
			#print data["title"]
			#json.dump(data, open(file, "w"), indent=4, separators=(',', ': '), sort_keys=True)
			#print ('mv -i "'+file+'" "0'+str(lineNumber)+" "+file+'"').replace("json/Бизнес-секреты/","")
		#lineNumber += 1
"""