## Sets

my_set = set()#Esto esun set
my_other_set = {}#Esto es un dictionary

print(type(my_set)) #type set
print(type(my_other_set)) #Inicialmente es un type dict

my_other_set ={"Raul", "Escobar", 31, 1.71}
print(type(my_other_set))# Ahora es un set

print(len(my_other_set)) #3

my_other_set.add('EscCode')
print(my_other_set)# Un set no es una estructura ordenada
#No se donde esta cada elemento, cambia de orden

my_other_set.add('EscCode')
print(my_other_set)# Un set no admite repetidos

print("Raul" in my_other_set)#Busca el elemento y devuelve true o false
print("Raule" in my_other_set)

my_other_set.remove("Raul")
print(my_other_set)

my_other_set.clear() #Vacia el set pero sigue existiendo
print(len(my_other_set))



del my_other_set #del es operacion del sistema elimina lo que sea

my_set = {'raul', 'escobar', 31}
my_list = list(my_set)
print(my_list)
print(my_list[0])#No hacer esto, ya que siempre cambia los lugares del set y no sabriamos cual qes el elemento 0 ni ningunmo
#No seas weon

my_other_set= {"Java", "Node", "Python"}

my_new_set = my_set.union(my_other_set) #union no modifica el set original
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', "C#"}))

print(my_new_set.difference(my_set))
