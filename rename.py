#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re

src="""Business Secrets - Filip Engelbert-o1pS92AG8xQ.mp4.info.json
Business Secrets - Guy Laliberte-KgonsWgYDTA.mp4.info.json
Business Secrets - Richard Branson-5H7FCbMEG3o.mp4.info.json
Business Secrets - Stephen Jennings-mg-I818saDg.mp4.info.json
Бизнес-секреты - Александр Акопов-DlpkVo8L59I.flv.info.json
Бизнес-секреты - Алексей Панферов-504IPjTXd34.mp4.info.json
Бизнес-секреты - Алексей Репик-jpdYTSbPU_A.mp4.info.json
Бизнес-секреты - Алла Вербер-Lsvwm-6wNVE.mp4.info.json
Бизнес-секреты - Андреас Рай-5JvQuPx6oDI.mp4.info.json
Бизнес-секреты - Андрей Даниленко-pBB3VY5c1-k.mp4.info.json
Бизнес-секреты - Анна Знаменская-qtvp-DrTVn8.mp4.info.json
Бизнес-секреты - Арам Мнацаканов-77KijruPOXA.mp4.info.json
Бизнес-секреты - Арас Агаларов-ulzJcKjU6ps.mp4.info.json
Бизнес-секреты - Артем Аветисян-s3BCNDe-2pM.mp4.info.json
Бизнес-секреты - Артемий Лебедев-MKoNHZbERMQ.mp4.info.json
Бизнес-секреты - Борис Йордан-_mBtu5JGCok.flv.info.json
Бизнес-секреты - Вадим Лапин-ig1gb2OvXkA.mp4.info.json
Бизнес-секреты - Вадим Финкельштейн-sP0XmK1dlsE.mp4.info.json
Бизнес-секреты - Всеволод Страх-lKtoMEkzchA.mp4.info.json
Бизнес-секреты - Дмитрий Маликов-dhdsa0L7gw4.mp4.info.json
Бизнес-секреты - Дмитрий Потапенко-k1lpX6Xv8as.flv.info.json
Бизнес-секреты - Евгений Каценельсон-1JFSWUIHGAs.mp4.info.json
Бизнес-секреты - Евгений Чичваркин-IdQrGkO6GM8.mp4.info.json
Бизнес-секреты - Елена Батурина-oipxvwjK8mE.mp4.info.json
Бизнес-секреты - Игорь Лейтис-jxYVSBiHPwk.mp4.info.json
Бизнес-секреты - Кирилл Андросов-UNxPixUG5Q4.mp4.info.json
Бизнес-секреты - Леонид Огородников-M57ZyeDXjo4.mp4.info.json
Бизнес-секреты - Леонид Шутов--VP7vghsoEU.mp4.info.json
Бизнес-секреты - Максим Иванов-08ijcWUdeLU.mp4.info.json
Бизнес-секреты - Максим Каширин-n-z9FnRXkXY.mp4.info.json
Бизнес-секреты - Максим Ноготков-ZuEQe-pixY0.mp4.info.json
Бизнес-секреты - Михаил Прохоров-JjOCjrebCwU.mp4.info.json
Бизнес-секреты - Ника Белоцерковская-SeRd38qbZvc.mp4.info.json
Бизнес-секреты - Николай Фоменко-GsCAgtODM2k.mp4.info.json
Бизнес-секреты - Олег Бойко-R_nuPRekJ-g.mp4.info.json
Бизнес-секреты - Олег Новиков-xXkQ5G823Ys.mp4.info.json
Бизнес-секреты - Оливер Хьюз-5QAL0R1wgOk.mp4.info.json
Бизнес-секреты - Ольга Слуцкер-VZLJs5ynLFQ.mp4.info.json
Бизнес-секреты - Сергей Мавроди-dnmgnDqKL9c.mp4.info.json
Бизнес-секреты - Сергей Матвиенко-l6kj7dqGN0Y.mp4.info.json
Бизнес-секреты - Сергей Петров-A12y4HSQ7DE.mp4.info.json
Бизнес-секреты - Сергей Полонский (1)-kj7BIqHYUj8.mp4.info.json
Бизнес-секреты - Сергей Полонский (2)-1xTUkxNDYpE.mp4.info.json
Бизнес-секреты - Федор Овчинников-cLtQHtS2W8k.mp4.info.json"""

result = string.split(src, '\n')

for line in result:
    print line
    res = re.sub('(Бизнес-секреты)|(Business Secrets)|( - )|(\.json)|(\.mp4)|(\.info)|(\.)', r'', line)
    print res
    res = string.split(res, '-')
    res = res[0]+".json"

    print res
    print ""