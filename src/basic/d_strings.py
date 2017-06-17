
#
# Strings in python uses "" or '' notation
first_name = 'Giovanni'
last_name = 'Aguirre'
print(first_name, last_name)

#
# Strings are immutable
name = 'Learning'
print('String id: ', id(name))
name += 'Python'  # Creates a new string
print('String id: ', id(name), '(New id created)')

#
# Strings behave as array
print('First position of name is: ', name[0])

#
# + is used to concatenate and * to repeat
print('\n+ means concat: a + b = ', 'a' + 'b')
print('* means repeat: "ab" * 3 = ', 'ab' * 3)

#
# You can slice string chars by range s[x:y]
print('\nname[0:3]:', name[0:3])
print('name[:3]: ', name[:3])
print('name[3:]: ', name[3:])

#
# ord() gets ASCII code of char
# chr() gets char represented by ASCII code
ascii = ord('C')
charf = chr(165)
print('\nASCII for "C":', ascii)
print('Char for "164"', charf)

#
# len() string length
# max() bigger char in strnig
# min() smallest char in string
print('\nLen of "Gio":', len("Gio"))
print('Max of "Gio":', max("Gio"))
print('Min of "Gio":', min("Gio"))

#
# You can use 'in' or 'not in' to check existence
# of string in another string. They are also known as
# membership operator
print('\n"Gio" in "Giovanni"', 'Gio' in 'Giovanni')
print('"Agui" not in "Giovanni"', 'Agui' not in 'Giovanni')

#
# You can use ( > , < , <= , <= , == , !=  ) to compare two strings.
# Python compares string lexicographically i.e using ASCII value
# of the characters.
print('\n"Gio" > "Agui" ?', 'Gio' > 'Agui')
