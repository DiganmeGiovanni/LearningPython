
#
# Opening a file
# f = open(filename, mode)
# Available modes are:
# 'r':  Read
# 'w':  Write
# 'a':  Append
# 'wb': Write in binary mode
# 'rb': Opens to read in binary mode

#
# Opening/Creating a file
file = open('data/file.txt', 'w')
file.write('ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
file.write('123456789\n')
file.write('lorem ipsum\n')
file.close()

#
# Reading file:

# file.read([number])
file = open('data/file.txt', 'r')
firstThree = file.read(3)
print('read(3): ', firstThree)
file.close()

# file.readline()
file = open('data/file.txt', 'r')
print('\nReading 2 lines: [readline()]')
line1 = file.readline()
line2 = file.readline()
print('Line 1: ', line1, end='')
print('Line 2: ', line2, end='')
file.close()

# Reading all the lines
file = open('data/file.txt', 'r')
lines = file.readlines()
print('\nAll lines in file as list:')
print(lines)
file.close()

#
# Appending data
file = open('data/file.txt', 'a')
newLine = input('\nEnter new file line: ')
newLine += '\n'
file.write(newLine)
file.close()

print('File contents:')
file = open('data/file.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')
