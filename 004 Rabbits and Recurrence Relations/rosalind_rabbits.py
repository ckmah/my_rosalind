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

