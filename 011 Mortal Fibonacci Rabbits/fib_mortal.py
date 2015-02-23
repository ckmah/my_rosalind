#!/usr/bin/env python
# author: Clarence Mah
# Given: Positive integers n <= 100 and m <= 20.
# Return: The total number of pairs of rabbits that will remain after the
# n-th month if all rabbits live for m months.

from sys import argv

script, filename = argv

f = open(filename)
args = f.read().split(' ')
months = int(args[0])
lifespan = int(args[1])
f.close()

# take advantage of memoization to reduce recursive runtime
rabbits = {0: 0, 1: 1}


def fib_mortal(m, life):
    """Return the total number of pairs of rabbits that will remain after
    the m-th month if all rabbits live for 'life' months.

    This method utilizes memoization with recursion for reasonable run times.

    The first few calulations are pure fibonacci before any rabbits die.
    """

    if m not in rabbits:
        if m <= life:
            rabbits[m] = fib_mortal(m - 1, life) + fib_mortal(m - 2, life)
        else:
            value = 0
            for x in range(2, life + 1):
                value += fib_mortal(m - x, life)
            rabbits[m] = value
    return rabbits[m]

print fib_mortal(months, lifespan)
