#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re, glob, json, sys
from pprint import pprint

def translit(locallangstring):
    conversion = {
        u'\u0410' : 'A',    u'\u0430' : 'a',
        u'\u0411' : 'B',    u'\u0431' : 'b',
        u'\u0412' : 'V',    u'\u0432' : 'v',
        u'\u0413' : 'G',    u'\u0433' : 'g',
        u'\u0414' : 'D',    u'\u0434' : 'd',
        u'\u0415' : 'E',    u'\u0435' : 'e',
        u'\u0401' : 'Yo',   u'\u0451' : 'yo',
        u'\u0416' : 'Zh',   u'\u0436' : 'zh',
        u'\u0417' : 'Z',    u'\u0437' : 'z',
        u'\u0418' : 'I',    u'\u0438' : 'i',
        u'\u0419' : 'Y',    u'\u0439' : 'y',
        u'\u041a' : 'K',    u'\u043a' : 'k',
        u'\u041b' : 'L',    u'\u043b' : 'l',
        u'\u041c' : 'M',    u'\u043c' : 'm',
        u'\u041d' : 'N',    u'\u043d' : 'n',
        u'\u041e' : 'O',    u'\u043e' : 'o',
        u'\u041f' : 'P',    u'\u043f' : 'p',
        u'\u0420' : 'R',    u'\u0440' : 'r',
        u'\u0421' : 'S',    u'\u0441' : 's',
        u'\u0422' : 'T',    u'\u0442' : 't',
        u'\u0423' : 'U',    u'\u0443' : 'u',
        u'\u0424' : 'F',    u'\u0444' : 'f',
        u'\u0425' : 'H',    u'\u0445' : 'h',
        u'\u0426' : 'Ts',   u'\u0446' : 'ts',
        u'\u0427' : 'Ch',   u'\u0447' : 'ch',
        u'\u0428' : 'Sh',   u'\u0448' : 'sh',
        u'\u0429' : 'Sch',  u'\u0449' : 'sch',
        u'\u042a' : '',    u'\u044a' : '',
        u'\u042b' : 'Y',    u'\u044b' : 'y',
        u'\u042c' : '',   u'\u044c' : '',
        u'\u042d' : 'E',    u'\u044d' : 'e',
        u'\u042e' : 'Yu',   u'\u044e' : 'yu',
        u'\u042f' : 'Ya',   u'\u044f' : 'ya',
    }
    translitstring = []
    for c in locallangstring:
        translitstring.append(conversion.setdefault(c, c))
    return ''.join(translitstring)

# resave json file
files = sorted(glob.glob("json/Бизнес-секреты/*.json"))
for file in files:

	json_data=open(file)
	data = json.load(json_data)
	json_data.close()

	#change data object here
	#data["number_in_playlist"] = str(data["number_in_playlist"])
	#data["raw_audio"] = u"Бизнес-секреты/"+data["number_in_playlist"].zfill(3)+" "+data["short_title"]+".m4a"
	#end of change data object

	#res = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '), encoding="utf-8", sort_keys=True)

	date = '%s-%s-%s'% (data["upload_date"][0:4], data["upload_date"][4:6], data["upload_date"][6:8])

	res = u"---\n"
	res += 'layout: post\n'
	res += 'comments: true\n'
	res += 'date: %s\n'% date
	res += 'title: "%s"\n'% data["short_title"]
	res += u'''categories:
- Все выпуски
'''
	for item in data:
	    #if item != "description":
	    value = ('%s'% data[item]).replace("\n","\\n").replace('"','\\"')
	    res += '%s: "%s"\n'% (item, value)
	res += "---\n\n"

	res +=	"{% img left "+data["thumbnail"]+" "+data["title"]+" %}\n"

	res += data["description"].replace('\n','  \n')

	newfile = "/home/roman/work/octopress/source/_posts/"+date+"-"+translit(data["short_title"]).replace(" ", "-").replace("(", "").replace(")", "")+".markdown"
	print newfile
	f = open(newfile, 'w+')
	f.write(res.encode("utf-8"))
	f.close()

	#print filename
# end resave json file


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

