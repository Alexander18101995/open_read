with open('1.txt', 'r', encoding = 'utf-8') as f:
  r = f.read()
with open('2.txt', 'r', encoding = 'utf-8') as ff:  
  rr = ff.read()
with open('3.txt', 'r', encoding = 'utf-8') as fff:  
  rrr = fff.read()
with open('z3.txt', 'w', encoding = 'utf-8') as f:
  f.write(rrr)
with open('z3.txt', 'a', encoding = 'utf-8') as f:
  f.write(rr)
with open('z3.txt', 'a', encoding = 'utf-8') as f:
  f.write(r)