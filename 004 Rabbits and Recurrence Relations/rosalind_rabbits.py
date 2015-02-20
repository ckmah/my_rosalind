# !/usr/bin/env python
# author: Clarence Mah
#Given: Positive integers n ≤ 40 and k ≤ 5.
#Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
from sys import argv

script, filename = argv

file = open(filename)
args = file.read().split(' ')
month = int(args[0])
litterSize = int(args[1])
file.close()

population = 1
immature = 0

for x in range(1, month):
    mature = population
    population = population + immature
    immature = litterSize * mature

print population

