# !/usr/bin/env python
# # author: Clarence Mah
# Given: Three positive integers k, m, and n, representing a population
#     containing k+m+n organisms: k individuals are homozygous dominant for a
#     factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will
#     produce an individual possessing a dominant allele (and thus
#     displaying the dominant phenotype). Assume that any two organisms can
#     mate.

import math
from sys import argv

script, filename = argv

data = open(filename).read().split(' ')

# k = homo dominant, m = heterozygous, n = homo recessive
k = int(data[0])
m = int(data[1])
n = int(data[2])
data.close()

total = float(k + m + n)

#probabilities of choosing specific genotype
probk = k/total
probm = m/total
probn = n/total
p = 1

# prob of hetero cross homo recessive, and homo recessive cross hetero
p -= (0.5)*probm*(n/(total - 1)) + (0.5)*probn*(m/(total - 1))

# prob of hetero cross hetero
p -= (0.25)*probm*((m - 1)/(total - 1))

# prob of homo recessive cross homo recessive
p -= probn*((n - 1)/(total - 1))

print p