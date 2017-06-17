""" Use of files in python
This module pretends shows the use of files and
its methods
"""

from __future__ import print_function

#
# Opening a file
# f = open(filename, mode)
# Available modes are:
# 'r':  Read
# 'w':  Write
# 'a':  Append
# 'wb': Write in binary mode
# 'rb': Opens to read in binary mode
file_name = './../../data/file_demo.txt'

# Opening/Creating/Writing a file
_file = open(file_name, 'w')
_file.write('ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
_file.write('123456789\n')
_file.write('lorem ipsum\n')
_file.close()


#
# Reading file:
#

# file.read([number])
_file = open(file_name, 'r')
firstThree = _file.read(3)
print ('First three chars: {}'.format(firstThree))
_file.close()

# file.readline()
_file = open(file_name, 'r')
print ('\nReading 2 lines with "readline()"')
line1 = _file.readline()
line2 = _file.readline()
print ('Line 1: {}'.format(line1), end='')
print ('Line 2: {}'.format(line2), end='')
_file.close()

# Reading all the lines
_file = open(file_name, 'r')
lines = _file.readlines()
print ('\nAll lines in file as list:')
print (lines)
_file.close()


#
# Appending data
#

# Append from user input
_file = open(file_name, 'a')
newLine = input('\nEnter new file line: ')
newLine += '\n'
_file.write(newLine)
_file.close()

# Iterating over file lines
print ('\nFile contents:')
_file = open(file_name, 'r')
lines = _file.readlines()
for line in lines:
    print (line, end='')

# Printing all lines
with open(file_name, 'r') as _file:
    print('\nAll contents:')
    for line in _file:
        print(line, end='')
