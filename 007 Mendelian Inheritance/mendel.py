# !/usr/bin/env python
# # author: Clarence Mah
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
from sys import argv

script, filename = argv

genotypes = open(filename).read().split(' ')

dom_homo = genotypes[0]
hetero = genotypes[1]
rec_homo = genotypes[2]

total_parents = dom_homo + hetero + rec_homo

total_offspring = math.factorial(total_parents)

dom_cross_all = (dom_homo*(hetero+rec_homo)+(math.factorial(dom_homo)/(math.factorial(dom_homo-2)*2)))

hetero_cross_rec_homo = 0.5*(hetero*rec_homo)
hetero_cross_hetero = 0.75(hetero - 1)

total_homo = dom_cross_all + hetero_cross_hetero + hetero_cross_rec_homo

prob_dom_phenotype = total_homo/total_offspring

print prob_dom_phenotype