my_list = ['banana', 'kiwi', 'apple', 'melon', 'peach']
print (str('Список :'),my_list)
print (str('Первый и последний элементы :'), my_list [2:5])
my_list [2] = ('lemon')
print (str('Замена яблока лимоном :'),my_list)


my_dict = {'apple': 'яблоко', 'banana': 'банан', 'kiwi': 'киви', 'melon': 'дыня', 'лимон': 'лимон'}
print (str('Словарь :'), my_dict)


print (my_dict ['apple'])
my_dict ['cherry'] ='вишня'
print (my_dict)

new_dict = {}
new_dict ['orange'] = 'апельсин'
my_dict .update(new_dict)
print (my_dict)