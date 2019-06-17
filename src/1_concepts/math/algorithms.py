""" Implementations of classic math algorithms """

from math import sqrt
from arithmetic import Operations
ops = Operations()


def pythagoras_hypotenuse(leg_a, leg_b):
    """ Calculates the hypotenuse of right triangle through
        pythagoras theorem
    """

    hypotenuse = sqrt((leg_a * leg_a) + (leg_b * leg_b))
    return hypotenuse


## Test
side_a = 3
side_b = 4
hyp = pythagoras_hypotenuse(side_a, side_b)
print 'Hypotenuse is: {}'.format(hyp)
