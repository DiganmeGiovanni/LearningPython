""" Implementation of pythagoras algorithm """
import sys

from operations import square_root
from operations import power
from operations import addition
from operations import subtract


def calc_hypotenuse(_side_a, _side_b):
    """ Calculates hypotenuse using theorem """
    return square_root(addition(
        power(_side_a, 2),
        power(_side_b, 2)
    ))


def calc_side(side, hypotenuse):
    """ Calculates a side through theorem """
    return square_root(subtract(
        power(hypotenuse, 2),
        power(side, 2)
    ))


def menu():
    print "                    "
    print "   |\\              "
    print "   |  \\ Hypotenuse "
    print " A |    \\          "
    print "   |______\\        "
    print "      B             "
    print "                    "
    print "Which triangle side do you want to calculate?"
    print "0. Exit program "
    print "1. Hypotenuse   "
    print "2. Side A       "
    print "3. Side B       "
    return input('Select an operation: ')


def main():
    option = menu()
    if option == 0:
        sys.exit(0)
    elif option == 1:
        side_a = float(input('Enter side a value: '))
        side_b = float(input('Enter side b value: '))
        print 'Hypotenuse is: {}'.format(calc_hypotenuse(side_a, side_b))
    elif option == 2:
        side_b = float(input('Enter side b value: '))
        hyp = float(input('Enter hypotenuse value: '))
        print 'Side A is: {}'.format(calc_side(side_b, hyp))
    elif option == 3:
        side_a = float(input('Enter side a value: '))
        hyp = float(input('Enter hypotenuse value: '))
        print 'Side B is: {}'.format(calc_side(side_a, hyp))
    else:
        print 'Enter a valid option'

    main()

main()
