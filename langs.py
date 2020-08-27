import json
import langdetect


# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))


langdetect.DetectorFactory.seed = 0
langs = {}

for file in data:
    print(file)
    for rec in data[file]:

        rec.replace('дата обращения','')

        try:
            lang = langdetect.detect_langs(data[file][rec]['1'])
            lng = (lang[0].lang)
            if lng in langs:
                langs[lng] +=1
            else:
                langs[lng]=1
        except:
            lang = []

    langs_sorted = sorted(langs, key=langs.get, reverse=True)

    for out in langs_sorted:
        print(out.strip() + ';' + str(langs[out]) + "")