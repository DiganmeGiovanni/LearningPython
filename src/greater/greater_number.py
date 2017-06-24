""" Determinate the greater of three numbers given by user """
import sys


def are_equal(a, b):
    return a == b


def greater(a, b):
    if a > b:
        return a
    return b


def main():
    print 'Lets to calculate the greater of three numbers'
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))
    c = float(input('Enter number 3: '))

    if are_equal(a, b) and are_equal(a, c):
        print 'Three numbers are equal'
    else:
        greater_number = greater(greater(a, b), c)
        print 'Greater number is: {}'.format(greater_number)

    print '\nCalculate again with different numbers?'
    print '1. Yes'
    print '2. No'
    opt = int(input('Type your option: '))
    if opt == 1:
        print ''
        main()
    else:
        print '\nGood bye :)'
        sys.exit(0)

main()
