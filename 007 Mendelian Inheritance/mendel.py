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


