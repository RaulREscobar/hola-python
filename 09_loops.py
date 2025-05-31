### Loops

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #Es opcional
    print('My condición es mayor o  iugal que 10')


print('La ejecución continua')


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('se detiene la ejecución')
        break #Para subitamente el bucle
    print(my_condition)

print('La ejecución continua')

##For

my_list = [25, 18, 25, 58, 30, 30]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, 'Raul', 'Escobar', 'Raul')
for element in my_list:
    print(element)

my_set ={"Raul", "Escobar", 31, 1.71}
for element in my_set:
    print(element)

my_dict = {'nombre':'Raul', 'Apellido': 'Escobar', 'Edad':31,'Lenguajes':{'Python', 'Swift', 'Kotlin'}, 1: 1.71 }
for element in my_dict:
    print(element)
    if element == 'Edad':
        break
else:
    print('El bucle for de diccionario ha finalizado')

print('La ejecución continua')

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('se ejecuta')
else:
    print('El bucle for de diccionario ha finalizado')