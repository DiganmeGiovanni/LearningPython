
#
# Defining methods for operators is known as operator overloading. For e.g.
# To use +  operator with custom objects  you need to define a method
# called __add__


from entities.models import SoftwareEngineer
from entities.models import Person

person1 = SoftwareEngineer('Giovanni', 24)
person2 = Person('Omar', 15)

print('Add:', person1 + person2)
print('<=:', person1 <= person2)
print('<:', person1 < person2)
print('>=:', person1 >= person2)
print('>:', person1 > person2)
