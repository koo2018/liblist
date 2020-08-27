import json,re

files = ['origins/mediacom_academ.txt','origins/mediacom_creative.txt','origins/jour_academ.txt','origins/jour_creative.txt',
         'origins_new/allbooks.txt','origins_new/mediacom.txt','origins_new/jour.txt']

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



for file in files:

    fl = open(file, 'r')
    lines = fl.readlines()

    a_names = []

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


        book_authors = res + res1 + res2 + res3
        #if book_authors: print(book_authors)
        for item in book_authors:
            item = item.replace(",",'')
            item = re.sub('\.$','',item).strip()+'.'
            if len(item.split()) > 1:
                name =  item.split()
                new_name = {'fam':'', 'in1':[]}
                for chast in name:
                    if not re.findall('[A-ZА-Я]\.',chast): new_name['fam'] = chast.replace('.','')
                    else: new_name['in1'].append(chast)
                    new_ini = ''
                    for ini in new_name['in1']:
                        new_ini += '. '.join(ini.split('.'))

                a_names.append(new_name['fam']+" "+new_ini)


        #print(res, res1, res2, res3, line,line1,line2,line3)

    top_a = {}
    for out in sorted(a_names):
        if  out not in top_a: top_a[out] = 1
        else: top_a[out] += 1

    top_a_sorted = sorted(top_a, key=top_a.get, reverse=True)
    fout  = open("authors/topauthor_"+file.split("/")[1]+".csv",'w')
    for out  in top_a_sorted:
        fout.write(out.strip()+';'+str(top_a[out])+"\n")

    fout.close()


