
#
# Generators are function used to create iterators,
# so that it can be used in the for loop.
#
# Verify prime numbers at: https://primes.utm.edu/lists/small/1000.txt


def is_prime(x):
    if x < 0 or x == 0:
        return False
    elif x == 1:
        return True
    else:
        divisible = False
        for i in range(2, x):
            if x % i == 0:
                divisible = True
                break
        return not divisible


def prime_numbers(start, stop):
    if start == stop:
        if is_prime(start):
            yield start
    elif stop < start:
        aux = stop
        stop = start
        start = aux

    i = start
    while i < stop:
        if is_prime(i):
            yield i
        i += 1


print('Prime numbers between 1 - 100')
for i in prime_numbers(1, 100):
    print(i)