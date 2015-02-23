# !/usr/bin/env python
# author: Clarence Mah
# Given: Positive integers n <= 40 and k <= 5.
# Return: The total number of rabbit pairs that will be present after n
# months if we begin with 1 pair and in each generation, every pair of
# reproduction-age rabbits produces a litter of k rabbit pairs (instead of
# only 1 pair).
from sys import argv

script, filename = argv

f = open(filename)
args = f.read().split(' ')
months = int(args[0])
litterSize = int(args[1])
f.close()

P = 1
F1 = 0

for x in range(1, months):
    mature = P
    P += F1
    F1 = litterSize * mature

print P
