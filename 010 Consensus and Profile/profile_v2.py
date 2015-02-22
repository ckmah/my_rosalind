# !/usr/bin/env python
# author: Clarence Mah
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
# in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If
# several possible consensus strings exist, then you may return any one of
# them.)

from sys import argv

script, filename = argv

fasta = open(filename)
text = fasta.readlines()
fasta.close()
seqs = []

# aggregate sequences into seqs list
for line in text:
    is_seq = line.find(">")
    seqs.append(line.strip()) if (is_seq == -1) else next

# matrix organized by list of bases at each index (# of sequences by
# sequence length)
matrix = zip(*seqs)

# creates profile matrix organized by list of counts of each base for each
# index (4 by sequence length)
profile = []
for line in matrix:
    profile.append(list(line.count(base) for base in 'ACGT'))

# create consensus from max of each position
consensus = ""
for position in profile:
    bases = 'ACGT'
    consensus += str(bases[(position.index(max(position)))])

print consensus

# print profile according to frequency of base occuring in each position
# of all sequences
for base_index in range(len(profile[0])):
    counts = 'ACGT'[base_index] + ":"
    for line in profile:
        counts += " " + str(line[base_index])
    print counts
