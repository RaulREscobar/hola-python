# tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Raul', 'Escobar', 'Raul')
my_other_tuple = (60,30, 50, 19, 44)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0]) 
print(my_tuple[-1]) 
#print(my_tuple[4]) error 
#print(my_tuple[-6]) error

print(my_tuple.count('Raul'))
print(my_tuple.index('Escobar'))
print(my_tuple.index('Raul'))

#my_tuple[1] = 1.80 Error

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'EscCode'
my_tuple.insert(1,'Black')
my_tuple = tuple(my_tuple) 
print(type(my_tuple))

# del my_tuple[2] Error
del my_tuple
#print(my_tuple) error elmina la variable

