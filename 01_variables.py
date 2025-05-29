# Variables = todo en minusculas y con '_' 

my_variable = 'My string Variable'
print(my_variable)

my_int_variable  = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_str_variable = str(my_int_variable)
print(my_int_str_variable)
print(type(my_int_str_variable))

#concatenar variables en print, pinta un string nuevo
print(my_variable, str(my_int_variable), my_bool_variable)

print("Este es el valor de:", my_bool_variable)

#Funciones de sistema

#lengt = contar caracteres
print(len(my_int_str_variable))

#variables en una sola linea, No abusar de esto.
name, surname, alias, age = 'Brias', 'Muere', 'Mueredev', 35
print('Me llamo:', name, surname,'. Mi alias es:',alias, '. Mi edad es: ',age)


#Inputs, piden información de la consola

name = input('Cual es tu nombre?')
age = input('Cuantos años tienes?')

print(name)
print(age)


#Cambiamos su tipo a las variables, no tiene tipado fuerte.

name= 35
age= "String"
print(name)
print(age)

#¿Forzamos el tipado? pero no detiene el codigo y no lo fuerza.
address: str = "Mi dirección" 
address = 25
address = False
address = 1.65
print(type(address))

