# Conditionals

my_condition = False

if my_condition: 
    print('Se ejecuta la condición del if')

my_condition = 5 * 5

if my_condition == 10: 
    print('Se ejecuta la condición del segundo if')

if my_condition > 10 and my_condition < 20: 
    print('Es mayor que diez y menor que 20')
elif my_condition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que diez o mayor o igual que 20 o distinto de 25')#los saltos de linea no modifican mientras este tabulado

print('La ejecuta continua')

my_str = ""
if not(my_str):
    print('My cadeno de texto esta vacia')

if my_str == 'My cadena de textoooooo':
    print('My cadeno de texto coinciden')