from pprint import pprint

cook_book = {}

with open('1.txt','r') as file:
  for line in file:
    name = line.strip()
    number = int(file.readline().strip())
    res = []
    for ingr in range(number):
      ingrs = {}
      ing = file.readline().split('|')
      ingrs['ingredient_name'] = ing[0].strip()
      ingrs['measure'] = ing[2].strip()
      ingrs['quantity'] = int(ing[1].strip())
      res.append(ingrs)
    file.readline()
    cook_book[name] = res 
pprint(cook_book)