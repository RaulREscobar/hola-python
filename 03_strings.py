###  Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"


print(len(my_string))
print(len(my_other_string))


print(my_string + " " + my_other_string)

my_new_line_string = "Este es un strin\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un strin con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \nescapado"
print(my_scape_string)


#Formateo

name, surname, age = 'Raul', 'Escobar', 32


print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print('Mi nombre es ' + name + " " + surname + ' y mi edad es ' +str(age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')


# Desempaquetado de caracteres
language = "python"
a, b, c, e, f, g = language

print(a)
print(b)

# Division

languaje_slice = language[1:3]
print(languaje_slice)

languaje_slice = language[1:]
print(languaje_slice)

languaje_slice = language[-2]
print(languaje_slice)

languaje_slice = language[0:6:2]
print(languaje_slice)

# Reverse

reversed_lenguaje = language[::-1]
print(reversed_lenguaje)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith('py')) #reconoce minusculas y mayusculas


