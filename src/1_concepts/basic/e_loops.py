""" Loops samples """
#
# Python has only 'for' and 'while' loops

#
# For loop
_len = int(input('Enter list len: '))
_list = []
for i in range(0, _len):
    prompt = 'Enter integer for pos ' + str(i) + ': '
    x = int(input(prompt))
    _list.append(x)

print('\nFinal list is:', list)
print 'Iterated list is:'
for i in _list:
    print i
print '\n'


#
# While loop
print '\nResuming count'
count = 0
while count < 5:
    count += 1
    print count

# break
print '\nResuming count'
while count < 10:
    count += 1
    print count
    if count == 7:
        print '\tDoing break'
        break

# Continue
print '\nResuming count'
while count < 15:
    count += 1
    if count == 10:
        print '\tDoing continue'
    else:
        print count
