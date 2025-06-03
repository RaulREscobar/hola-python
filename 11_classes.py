### Classes
##Clases se escriben en CamelCase
class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f'{name} {surname} ({alias})' #Propiedad publica
        self.__name = name #Propiedad Privada
        self.__surname = surname
    
    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname
    
    def walk (self): 
        print(f'{self.full_name} está caminando')

my_person = Person('Raul', 'Escobar')

print(my_person.full_name)
my_person.walk()


my_other_person = Person('Pepito', 'Pedro', 'Pepe')

print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 'Juan Carlos (El Gaucho)'
print(my_other_person.full_name)
print(my_other_person.get_name())
print(my_other_person.get_surname())

my_other_person.full_name = 666
print(my_other_person.full_name)