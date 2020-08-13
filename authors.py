import json


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
