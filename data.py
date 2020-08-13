import json

# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))

print(data)