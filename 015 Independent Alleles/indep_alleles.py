# !/usr/bin/env python
# author: Clarence Mah
# Given: Two positive integers k (k<=7) and N (N<=2k). In this problem, we
# begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two
# children in the 1st generation, each of whom has two children, and so on.
# Each organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to
# the k-th generation of Tom's family tree (don't count the Aa Bb mates at
# each level). Assume that Mendel's second law holds for the factors.
from sys import argv
from scipy import misc

script, filename = argv
f = open(filename)
data = f.readline().split()
f.close()

# number of generations
gens = int(data[0])
# minimum number of organisms for genotype AaBb
n = int(data[1])


def prob(n, k):
    return (misc.comb(k, n) * 0.25**n * 0.75**(k - n))

output = 1 - sum([prob(i, 2**gens) for i in range(n)])
print round(output, 3)
