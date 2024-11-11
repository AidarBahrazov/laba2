# 2.2 Аргументы и параметры функции

def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}


my_cat = cat(color = 'Grey', age = 9, name = 'Alise')
print(my_cat)