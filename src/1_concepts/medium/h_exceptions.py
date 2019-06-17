
from entities.exceptions import DrinkException
from entities.models import Person

# Create two persons
person1 = Person('Giovanni', 24)
person2 = Person('Omar', 15)

# Tries take a drink over two persons
try:
    person1.take_drink()
    person2.take_drink()
except DrinkException as ex:
    print('DrinkException: ', ex)
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")
