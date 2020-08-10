import re
import shutil
import json
from urllib.parse import urlparse
from dateutil import parser


files = ['origins/mediacom_academ.txt','origins/mediacom_creative.txt','origins/jour_academ.txt','origins/jour_creative.txt']
data = dict()
cnt = 0

'''
Ниже - специальный блок, чтобы из исходных файлов сделать общие файлы: 
вообще общеий, общий по журу и общий по медиакому. 
Если исходники не менялись, можно оставлять задокументированным
'''


with open('origins_new/allbooks.txt', 'w') as wfd:
    for f in files:
        with open(f,'r') as fd:
            shutil.copyfileobj(fd, wfd)

with open('origins_new/mediacom.txt', 'w') as wfd:
    for f in ['origins/mediacom_academ.txt','origins/mediacom_creative.txt']:
        with open(f,'r') as fd:
            shutil.copyfileobj(fd, wfd)

with open('origins_new/jour.txt', 'w') as wfd:
    for f in ['origins/jour_academ.txt','origins/jour_creative.txt']:
        with open(f,'r') as fd:
            shutil.copyfileobj(fd, wfd)



files.append('origins_new/allbooks.txt')
files.append('origins_new/mediacom.txt')
files.append('origins_new/jour.txt')


for file in files:



    fin = open(file, 'r')
    cnt = 0
    years =  list()
    file_data = dict()
    year_kolvo = dict()

    for line in fin:

        line_orig = line
        # чистимся
        line = re.sub('\d\d\.\d\d\.\d{4}', '', line)
        line = re.sub('(?P<url>https?:\/\/[^\s^\n]+)', '', line)
        line = re.sub('(?P<url>www\.[^\s^\n]+)', '', line)
        #line = re.sub('\d{1,4}\-\d{1,4}', '', line)
        line = re.sub('[N\#\№]\s?\d{4}', '', line)
        line = re.sub('(doi|DOI).*$', '', line)
        line = re.sub('(ISBN|isbn).*$', '', line)
        line = re.sub('^\d{4}', '', line)


        result = list(set(re.findall('[12][90]\d{2}', line)))

        result_url = re.findall('https?\:.*$', line_orig)
        a=''
        if result_url:

            urls = re.split('[\s\)\,\>\(]', result_url[0])

            for url in urls:
                if 'http' in url: a = url

        if a:
            url_parse = urlparse(a)
            b = (re.split('(www\.)|(web\.)', url_parse.netloc)[-1])
            #b = '.'.join(url_parse.netloc.split('.')[-2::])
        else: b = ''

        date_obr = re.findall('\:\s\d{1,2}\.\d{2}\.\d{4}',line_orig)[-1:]


        if date_obr:


            parsed = re.sub('(\d{1,2})\.(\d{2})\.(\d{4})','\g<3>-\g<2>-\g<1>',date_obr[0]).replace(": ",'')


            try:
                parsed = parser.parse(parsed)
            except:
                parsed = 'Unexisting date!'


            cnt += 1
        else: parsed = ''


        date_obr = re.findall('\(accessed\s\d{1,2}\s[a-zA-Z]*\s\d{4}\)', line_orig)
        if date_obr:

            new_str = date_obr[0].replace('(accessed ','').replace(')','')

            parsed = parser.parse(new_str)

            cnt += 1


        file_data[cnt]={0:line_orig,1:line,2:result,3:a,4:b,5:str(parsed)}


        for year in result:

            years.append(year)

        cnt += 1


    for year in years:
        if int(year) < 2021:

            if year not in year_kolvo:
                year_kolvo[year] = 1
            else:
                year_kolvo[year] += 1

    #for year in sorted(year_kolvo, reverse=True):
        #print(year,":",year_kolvo[year])

    fin.close()
    data[file] = file_data

    #print(data)

print(cnt)

# Сохраняем словарь в файл
with open('data.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(data))

