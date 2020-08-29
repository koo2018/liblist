import json,re
import langdetect


# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))


langdetect.DetectorFactory.seed = 0
langs = {}

file = 'origins/jour_creative.txt'
print(file)
cnt = 1
for rec in data[file]:

    try:
        lang = langdetect.detect_langs(data[file][rec]['0'])
        lng = (lang[0].lang)
        if lng in langs:
            langs[lng] +=1
        else:
            langs[lng]=1

        if "bg:" in str(lang[0]):
            print(cnt, data[file][rec]['0'].strip())
            cnt += 1
    except:
        lang = []

'''


    langs_sorted = sorted(langs, key=langs.get, reverse=True)

    for out in langs_sorted:

        print(out.strip() + ';' + str(langs[out]) + "")

'''
