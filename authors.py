import json,re

'''
# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))

with open('authors/authors.txt', 'r') as auth_f:
    authors = auth_f.readlines()


for person in authors:
    pers = person.split()[0].strip()+" "+person.split()[1].strip()[:1]+"."
    for dt in data:

        for dt1 in data[dt]:
            if pers in data[dt][dt1]['0']:
                print (str(dt).split("/")[1], person.strip(), "=>", data[dt][dt1]['0'])
                
'''

fl = open('origins_new/allbooks.txt', 'r')
lines = fl.readlines()

for line in lines:
    # Куприянов А. М.
    res = re.findall('[A-ZА-Я][-a-zа-яü]*,?\s?[A-ZА-Я]\.\s?[A-ZА-Я]\.',line)
    line1 = line
    if res:
        for r in res:
            line1 = line1.replace(r,'')
            line1 = re.sub('\s+', ' ', line1).strip()

    # Куприянов А.
    res2 = re.findall('[A-ZА-Я][-a-zа-яü]*,?\s?[A-ZА-Я]\.',line1)

    line2 = line1
    if res2:
        for r in res2:
            line2 = line2.replace(r, '')
            line2 = re.sub('\s+', ' ', line2).strip()

    # А. М. Куприянов
    res1 = re.findall('[A-ZА-Я]\.\s?[A-ZА-Я]?\.?\s[A-ZА-Я][-a-zа-яü]*\.?', line2)

    line3 = line2
    if res1:
        for r in res1:
            line3 = line3.replace(r, '')
            line3 = re.sub('\s+', ' ', line3).strip()

    # А. М. Куприянов
    res3 = re.findall('[A-ZА-Я]\.\s?[A-ZА-Я]?\.?\s[-a-zа-яü]*\.?', line3)


    print(res + res1 + res2+res3)
    print(res, res1, res2, res3, line,line1,line2,line3)
    print()


