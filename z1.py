def cook_book(): 
  f = open('1.txt','r', encoding = 'utf-8') 
  r_0 = f.readline().strip()
  r_1 = f.readline()
  r_2 = f.readline()
  r_3 = f.readline()
  r_4 = f.readline()
  r_5 = f.readline()
  r_6 = f.readline().strip()
  r_7 = f.readline()
  r_8 = f.readline()
  r_9 = f.readline()
  r_10 = f.readline()
  r_11 = f.readline()
  r_12 = f.readline()
  r_13 = f.readline().strip()
  r_14 = f.readline()
  r_15 = f.readline()
  r_16 = f.readline()
  r_17 = f.readline()
  keys = ['ingridient_name', 'quantity', 'measure']
  cook_book = {}
  cook_book[r_0] = []
  omelet = []
  omelet.append(r_2[0:5])
  omelet.append(r_2[7:8])
  omelet.append(r_2[11:13])
  omelet_1 = []
  omelet_1.append(r_3[0:6])
  omelet_1.append(r_3[9:12])
  omelet_1.append(r_3[15:17])
  omelet_2 = []
  omelet_2.append(r_4[0:7])
  omelet_2.append(r_4[10:11])
  omelet_2.append(r_4[14:16])
  omelet_dict = dict(zip(keys,omelet))
  omelet_dict_1 = dict(zip(keys,omelet_1))
  omelet_dict_2 = dict(zip(keys,omelet_2))
  cook_book[r_0] = [omelet_dict,omelet_dict_1,omelet_dict_2,]
  cook_book[r_6] = []
  peking_duck = []
  peking_duck.append(r_8[0:4])
  peking_duck.append(r_8[7:8])
  peking_duck.append(r_8[11:13])
  peking_duck_1 = []
  peking_duck_1.append(r_9[0:4])
  peking_duck_1.append(r_9[7:8])
  peking_duck_1.append(r_9[11:12])
  peking_duck_2 = []
  peking_duck_2.append(r_10[0:3])
  peking_duck_2.append(r_10[6:7])
  peking_duck_2.append(r_10[10:14])
  peking_duck_3 = []
  peking_duck_3.append(r_11[0:11])
  peking_duck_3.append(r_11[14:16])
  peking_duck_3.append(r_11[19:21])
  pd = dict(zip(keys,peking_duck))
  pd_1 = dict(zip(keys,peking_duck_1))
  pd_2 = dict(zip(keys,peking_duck_2))
  pd_3 = dict(zip(keys,peking_duck_3))
  cook_book[r_6] = [pd,pd_1,pd_2,pd_3]
  cook_book[r_13] = []
  baked_potatoes = []
  baked_potatoes.append(r_15[0:9])
  baked_potatoes.append(r_15[12:13])
  baked_potatoes.append(r_15[16:18])
  baked_potatoes_1 = []
  baked_potatoes_1.append(r_16[0:6])
  baked_potatoes_1.append(r_16[9:10])
  baked_potatoes_1.append(r_16[13:17])
  baked_potatoes_2 = []
  baked_potatoes_2.append(r_17[0:9])
  baked_potatoes_2.append(r_17[12:15])
  baked_potatoes_2.append(r_17[18:19])
  bd = dict(zip(keys,baked_potatoes))
  bd_1 = dict(zip(keys,baked_potatoes_1))
  bd_2 = dict(zip(keys,baked_potatoes_2))
  cook_book[r_13] = [bd,bd_1,bd_2]
  print(cook_book)
cook_book()