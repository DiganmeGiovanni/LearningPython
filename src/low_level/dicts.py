""" Use of strings in python
This module pretends shows the use of strings and its
operations in python
"""

# Dicts are iterable by nature
data_dict = {
    'first_name': 'Giovanni',
    'last_name': 'Aguirre',
    'age': 24,
    'passions': ('Music', 'Software development', 'Bikes')
}

# Iterate looking for age
for key in data_dict:
    if key == 'age':
        print 'Age is: {}'.format(data_dict[key])
