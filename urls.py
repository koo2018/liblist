import re
import json

# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))

files = ['origins/mediacom_academ.txt','origins/mediacom_creative.txt','origins/jour_academ.txt','origins/jour_creative.txt',
         'origins_new/allbooks.txt','origins_new/mediacom.txt','origins_new/jour.txt']

'''
Топ ссылок
'''



for file in files:
    url_top = {}

    for smf in data[file]:

        url = data[file][smf]['4']
        if url:
            if url not in url_top:
                url_top[url] = 1
            else:
                url_top[url] += 1

    print(file)
    url_top_sorted = sorted(url_top, key=url_top.get, reverse=True)

    for url in url_top_sorted:
        print(url+":", url_top[url])

'''
    топ youtube
'''



for file in files:
    yt_top = {}

    for smf in data[file]:

        url = data[file][smf]['3']
        if url:

            if 'youtube.com' in url or 'youtu.be' in url:
                if url not in yt_top:
                    yt_top[url] = 1
                else:
                    yt_top[url] += 1

    print(file)

    yt_top_sorted = sorted(yt_top, key=yt_top.get, reverse=True)

    for url in yt_top_sorted:
        print(url+":", yt_top[url])




upon_years = dict()

for file_name in data:
    upon_years[file_name] = {}
    for nomer in data[file_name]:

        year_list = data[file_name][nomer]['2']



        for year in year_list:

            if year not in upon_years[file_name]:
                upon_years[file_name].update({year:[data[file_name][nomer]['0']]})

            else:
                upon_years[file_name][year].append(data[file_name][nomer]['0'])


'''
Ссылки    
'''


for file_name in data:
    file_name = 'origins/jour_academ.txt'


    for smf in upon_years[file_name]:

        for record in upon_years[file_name][smf]:

            result = re.findall('https?\:.*$', record)

            if result:

                urls = re.split('[\s\)\,\>\(]',result[0])

                for url in urls:
                    if 'http' in url: a = url

                #print(a)


    break
