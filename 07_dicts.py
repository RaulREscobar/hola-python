### Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'nombre':'Raul', 'Apellido': 'Escobar', 'Edad':31, 1:'Python'}

my_dict = {
    'nombre':'Raul', 
    'Apellido': 'Escobar', 
    'Edad':31,
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1: 1.71,
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['nombre'])

my_dict['nombre'] = 'Pedro'
print(my_dict['nombre'])

print(my_dict[1])

my_dict['Calle'] = "Calle casa"
print(my_dict['Calle'])

del my_dict['Calle']#No se recuperan los del
print(my_dict)

print('Raul' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['nombre', 1, 'Piso']
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)

my_new_dict = dict.fromkeys(('nombre', 1, 'Piso')) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))


my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
