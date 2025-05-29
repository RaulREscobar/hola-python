#Operadores aritmeticos

print(5 + 6)#Suma
print(5 - 6)#Resta
print(5 * 6)#División
print(5 / 6)#Diisión
print(5 % 6)#Modulo
print(5 // 6)#flor división, devuelve un numero entero, redondea
print(5 ** 6)#exponente
print(5 ** 6 +5 -6 // 2 * 2)#se pueden conbinar


print('Hola ' + 'Python') #Solo concatena texto, no resta, ni otro operador
print('Hola ' + str(5)) #No se mezclan tipos de datos
print('Hola ' * 5) #Se repiten el string, siempre que se mutiplique por enteros

my_float = 2.5 * 2
print('Hola ' * int(my_float))#Podemos pasarlo a entero

#Operadores Comparativos
print(5 > 6)#menor
print(5 < 6)#Resta
print(5 >= 6)#mayor o igual
print(5 <= 6)#menor o igual
print(5 == 6)#igual
print(5 != 6)#diferente


#Compara 
print('Hola' > 'Python')#menor
print('Hola' < 'Python')#Resta
print('Hola' >= 'Python')# Compara ordenación alfabetica, incluye las mayusculas Por ASCII
print(len('Hola') <= len('Python'))#Cuenta caracteres
print('Hola' == 'Python')#igual
print('Hola' != 'Python')#dstinto


#Operadores Logicos

print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')

print(3 < 4 and 'Hola' < 'Python')
print(3 > 4 or 'Hola' < 'Python')
print(3 > 4 or ('Hola' < 'Python' and 4 == 4))

print(not(3 > 4))