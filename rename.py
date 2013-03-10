#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re, glob, json, sys
from pprint import pprint

src="""001-Бизнес-секреты - Борис Йордан-_mBtu5JGCok.m4a
002-Бизнес-секреты - Анна Знаменская-qtvp-DrTVn8.m4a
003-Бизнес-секреты - Михаил Прохоров-JjOCjrebCwU.m4a
004-Бизнес-секреты - Олег Бойко-R_nuPRekJ-g.m4a
005-Бизнес-секреты - Николай Фоменко-GsCAgtODM2k.m4a
006-Бизнес-секреты - Артемий Лебедев-MKoNHZbERMQ.m4a
007-Бизнес-секреты - Оливер Хьюз-5QAL0R1wgOk.m4a
008-Business Secrets - Richard Branson-5H7FCbMEG3o.m4a
009-Бизнес-секреты - Сергей Мавроди-dnmgnDqKL9c.m4a
SeRd38qbZvc-Бизнес-секреты - Ника Белоцерковская.webm
IdQrGkO6GM8-Бизнес-секреты - Евгений Чичваркин.webm
l6kj7dqGN0Y-Бизнес-секреты - Сергей Матвиенко.webm
1JFSWUIHGAs-Бизнес-секреты - Евгений Каценельсон.webm
A12y4HSQ7DE-Бизнес-секреты - Сергей Петров.webm
ulzJcKjU6ps-Бизнес-секреты - Арас Агаларов.webm
xXkQ5G823Ys-Бизнес-секреты - Олег Новиков.webm
oipxvwjK8mE-Бизнес-секреты - Елена Батурина.webm
dhdsa0L7gw4-Бизнес-секреты - Дмитрий Маликов.mp4
504IPjTXd34-Бизнес-секреты - Алексей Панферов.webm
ZuEQe-pixY0-Бизнес-секреты - Максим Ноготков.webm
REG3VadrGto-Бизнес-секреты - Майкл Калви.webm
cLtQHtS2W8k-Бизнес-секреты - Федор Овчинников.webm
jxYVSBiHPwk-Бизнес-секреты - Игорь Лейтис.webm
-VP7vghsoEU-Бизнес-секреты - Леонид Шутов.webm
sP0XmK1dlsE-Бизнес-секреты - Вадим Финкельштейн.webm
o1pS92AG8xQ-Business Secrets - Filip Engelbert.webm
mg-I818saDg-Business Secrets - Stephen Jennings.webm
77KijruPOXA-Бизнес-секреты - Арам Мнацаканов.webm
5JvQuPx6oDI-Бизнес-секреты - Андреас Рай.webm
s3BCNDe-2pM-Бизнес-секреты - Артем Аветисян.webm
M57ZyeDXjo4-Бизнес-секреты - Леонид Огородников.webm
kj7BIqHYUj8-Бизнес-секреты - Сергей Полонский (1).webm
KgonsWgYDTA-Business Secrets - Guy Laliberte.webm
1xTUkxNDYpE-Бизнес-секреты - Сергей Полонский (2).webm
UNxPixUG5Q4-Бизнес-секреты - Кирилл Андросов.webm
08ijcWUdeLU-Бизнес-секреты - Максим Иванов.webm
ig1gb2OvXkA-Бизнес-секреты - Вадим Лапин.webm
VZLJs5ynLFQ-Бизнес-секреты - Ольга Слуцкер.webm
n-z9FnRXkXY-Бизнес-секреты - Максим Каширин.webm
jpdYTSbPU_A-Бизнес-секреты - Алексей Репик.mp4
Lsvwm-6wNVE-Бизнес-секреты - Алла Вербер.webm
pBB3VY5c1-k-Бизнес-секреты - Андрей Даниленко.webm
lKtoMEkzchA-Бизнес-секреты - Всеволод Страх.webm
k1lpX6Xv8as-Бизнес-секреты - Дмитрий Потапенко.webm
DlpkVo8L59I-Бизнес-секреты - Александр Акопов.webm"""

src = string.split(src, '\n')


# resave json file
files = sorted(glob.glob("json/Бизнес-секреты/*.json"))
for file in files:
	print file
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()

	#change data object here
	data["number_in_playlist"] = str(data["number_in_playlist"])
	data["raw_audio"] = "Бизнес-секреты/"+data["number_in_playlist"].zfill(3)+data["short_title"]+"m4a"

	res = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '), encoding="utf-8", sort_keys=True)
	f = open(file, 'w')
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