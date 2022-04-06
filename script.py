import json
from pprint import pprint

with open('cook_book.txt','r', encoding='cp1251') as f:
    r = f.read()
    print(r)

with open('cb.json','w') as fr:
     json.dump(r,fr, ensure_ascii=False, indent = 4)

    