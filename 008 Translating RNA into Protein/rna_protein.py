# !/usr/bin/env python
# # author: Clarence Mah

from sys import argv

script, filename = argv

# read in RNA
rna = open(filename)
seq = rna.readline().strip('\n')
rna.close()

# read in codon table
table = open("protein_table_sorted.txt")
codons = table.readlines()
table.close()

codon_map = {}

# create dictionary from codon table
for line in codons:
    keyval = line.split(' ')
    codon_map[keyval[0]] = keyval[1].strip('\n')

polyp = ""

# use dictionary to look up each codon
for x in range(0,len(seq),3):
    protein = codon_map[seq[x:x + 3]]
    if protein == 'Stop':
        break
    else:
        polyp += codon_map[seq[x:x + 3]]

print polyp