import re
import json
import difflib


# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))

files = ['origins/mediacom_academ.txt','origins/mediacom_creative.txt','origins/jour_academ.txt','origins/jour_creative.txt',
         'origins_new/allbooks.txt','origins_new/mediacom.txt','origins_new/jour.txt']

'''
Года
'''


for file in files:
    print(file)

    years = {}
    for item in (data[file]):
        new_line = re.sub('\d{4}[\-\–]\d{4}','',data[file][item]['1'].strip())
        #print(new_line)
        yr = list(set(re.findall('[\s,(-]([12]\d{3})',new_line)))
        #print(yr)
        for y in yr:
            if y in years: years[y] += 1
            else: years[y] = 1

        #print()

    top_years_sorted = sorted(years, key=years.get, reverse=True)

    fout = open('books/topyears_' + file.split('/')[1] + ".csv", 'w', encoding='cp1251')

    for y in top_years_sorted:
        fout.write(y + ';' + str(years[y]) + '\n')

    fout.close()



for file in files:

    strings = []

    books = {}

    cnt = 0

    print(file)

    for item in (data[file]):

        strings.append(data[file][item]['0'].lower().strip())

    for book in set(strings):

        books[book] = strings.count(book)
        if books[book] >1: print(book,books[book])






    break





    print(strings)
