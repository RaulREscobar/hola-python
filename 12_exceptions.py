### Exceptions Handlings ###

number_one, number_two = 5, 1

#number_two = '6'

## try except
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    ##esto se ejecuta si se produce una except
    print('Se ha producido un error')

## try except else

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    print('Se ha producido un segundo error')
else:
    ##esto se ejecuta si no se produce una except
    print('La ejecución continua correctamente')



## try except else finally
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    print('Se ha producido un segundo error')
else:#optional
    ##esto se ejecuta si no se produce una except
    print('La ejecución continua correctamente')
finally:#optional
    # Se ejecuta siempre
    print('La ejecución Continúa en el finally')



#Captura de exception por type

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError:
    ##esto se ejecuta si se produce una except ValueError
    print('Se ha producido un ValueError')
except TypeError:
    ##esto se ejecuta si se produce una except TypeError
    print('Se ha producido un TypeError')



#Captura de la información de la excepción
number_two = '6'
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError as error:
    print(error.args)
except Exception as err:
    print(err)
