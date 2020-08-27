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

    fout = open('urls/topsites_'+file.split('/')[1]+".csv", 'w')

    for url in url_top_sorted:
        fout.write(url+"; "+str(url_top[url])+'\n')

    fout.close()

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



    yt_top_sorted = sorted(yt_top, key=yt_top.get, reverse=True)

    fout = open('urls/youtube_' + file.split('/')[1] + ".csv", 'w')

    for url in yt_top_sorted:
        fout.write(url+"; "+str(yt_top[url])+'\n')

    fout.close()


'''
    топ telegram
'''

for file in files:
    tlg_top = {}

    for smf in data[file]:

        url = data[file][smf]['3']
        if url:

            if '//t.me/' in url:
                if url not in tlg_top:
                    tlg_top[url] = 1
                else:
                    tlg_top[url] += 1



    tlg_top_sorted = sorted(tlg_top, key=tlg_top.get, reverse=True)

    fout = open('urls/tlg_' + file.split('/')[1] + ".csv", 'w')

    for url in tlg_top_sorted:
        fout.write(url+"; "+str(tlg_top[url])+'\n')

    fout.close()

'''
    топ vk
'''

for file in files:
    vk_top = {}

    for smf in data[file]:

        url = data[file][smf]['3']
        if url:

            if '//vk.com/' in url:
                if url not in vk_top:
                    vk_top[url] = 1
                else:
                    vk_top[url] += 1



    vk_top_sorted = sorted(vk_top, key=vk_top.get, reverse=True)

    fout = open('urls/vk_' + file.split('/')[1] + ".csv", 'w')

    for url in vk_top_sorted:
        fout.write(url+"; "+str(vk_top[url])+'\n')

    fout.close()



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

top_urls = {}
for file_name in data:

    for smf in upon_years[file_name]:

        for record in upon_years[file_name][smf]:

            result = re.findall('https?\:.*$', record)

            if result:

                urls = re.split('[\s\)\,\>\(]',result[0])

                for url in urls:
                    if 'http' in url: a = url


                if a in top_urls:
                    top_urls[a] += 1
                else:
                    top_urls[a] = 1

    top_urls_sorted = sorted(top_urls, key=top_urls.get, reverse=True)

    fout = open('urls/topurls_' + file_name.split('/')[1] + ".csv", 'w',encoding='cp1251')

    for url in top_urls_sorted:
        fout.write(url+';'+str(top_urls[url])+'\n')

    fout.close()
