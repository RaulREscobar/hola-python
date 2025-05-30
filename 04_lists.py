### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [25, 18, 25, 58, 30, 30]

print(len(my_list))

my_other_list = [35, 1.77, 'Raul', 'Esco']

print(type(my_list)) #Type list
print(type(my_other_list)) #Type list

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) #cuenta desde atras
print(my_other_list[-3]) #cuenta desde atras
print(my_other_list.count("Raul")) #Retorna el numero de ocurrencia del elemento del parametro  
print(my_list.count(30)) #Cuenta el elemento del parametro  
#print(my_other_list[4]) index error
#print(my_other_list[-5]) index error

age, height, name, surname = my_other_list #necesita todos los elementos
print(name)


print(my_list + my_other_list)#Concatenar listas
#print(my_list - my_other_list) error

my_other_list.append('EscCode')
print(my_other_list)
my_other_list.insert(1,'rojo')
print(my_other_list)

my_other_list[1] = 'azul'
print(my_other_list)

my_other_list.remove('azul')
print(my_other_list)


my_list.remove(30)#Remueve por valor, el primero que encuentre
print(my_list)

my_list.pop()
print(my_list)

print(my_list.pop())

print(my_list.pop(2))

my_pop_element = my_list.pop(1)
print(my_pop_element)

del my_list[0] #Elimina el indice
print(my_list)

my_list.append(5)
my_list.append(36)
my_list.append(40)
my_list.append(15)
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = 'Hola Python'
print(my_list)
print(type(my_list))


