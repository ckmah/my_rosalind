# !/usr/bin/env python
# # author: Clarence Mah
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
from sys import argv

script, filename = argv

population = open(filename).read().split(' ')

dominant = population[0]
heterozygous = population[1]
recessive = population[2]

genotypes = []

for count in range(0, dominant):
    genotypes.append('AA')

for count in range(0, heterozygous):
    genotypes.append('Aa')

for count in range(0, recessive):
    genotypes.append('aa')


