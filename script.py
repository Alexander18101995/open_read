
k = ['ingredient_name','quantity','measure']
t = ['Яйцо',2,'шт']
k_2 = ['ingredient_name','quantity','measure']
t_2 =['Молоко',100,'шт']
k_3 = ['ingredient_name','quantity','measure']
t_3 =['Помидор',2,'шт']
t_dict = dict(zip(k,t))
t_dict_2 = dict(zip(k_2,t_2))
t_dict_3 = dict(zip(k_3,t_3))
cb = [t_dict,t_dict_2,t_dict_3]

#print(t_dict)
#print(t_dict_2)
#print(t_dict_3)
#print(cb_i_n)
print(cb) 



#'Омлет': [
# {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
# {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
# {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#]
