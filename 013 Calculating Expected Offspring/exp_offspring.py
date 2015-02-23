# !/usr/bin/env python
# author: Clarence Mah
# Given: Six positive integers, each of which does not exceed 20,000. The
# integers correspond to the number of couples in a population possessing
# each genotype pairing for a given factor. In order, the six given integers
# represent the number of couples having the following genotypes:
#   AA-AA
#   AA-Aa
#   AA-aa
#   Aa-Aa
#   Aa-aa
#   aa-aa
# Return: The expected number of offspring displaying the dominant
# phenotype in the next generation, under the assumption that every couple
# has exactly two offspring.

from sys import argv

script, filename = argv
f = open(filename)
data = f.readline().split(' ')

# number of offspring per couple
offspring = 2

zero = 1 * int(data[0]) * offspring
one = 1 * int(data[1]) * offspring
two = 1 * int(data[2]) * offspring
three = 0.75 * int(data[3]) * offspring
four = 0.5 * int(data[4]) * offspring
five = 0 * int(data[5]) * offspring

print (zero + one + two + three + four + five)
