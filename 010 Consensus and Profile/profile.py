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

# 2 way base-to-index map
base_index_map = {
    'A': 0, 'C': 1, 'G': 2, 'T': 3, 0: 'A', 1: 'C', 2: 'G', 3: 'T'}

# 4 by "sequence length" matrix (each line represents a different base
# A, C, G, or T) to track base frequencies for each position across all
# sequences
profile = [[0 for _ in range(len(seqs[0]))] for _ in range(4)]

# iterate over each sequence line, then each index; increment base
# frequencies accordinglye
for line in seqs:
    for line_base_index in range(len(line)):
        # use base_index_map to determine correct base
        profile_base = base_index_map[line[line_base_index]]
        profile[profile_base][line_base_index] += 1

consensus = ""
base_counts = []

# determine possible consensus string by iterating over each index of each line
for index in range(len(profile[0])):
    for profile_base in profile:
        # aggregate counts of each base at pos 'index' across all sequences
        base_counts.append(profile_base[index])

    # find most represented base listed first for pos 'index'
    max_base_index = base_counts.index(max(base_counts))
    base_counts = []
    consensus += base_index_map[max_base_index]

print consensus

for line_index in range(len(profile)):
    frequencies = ""
    for base_freq in profile[line_index]:
        frequencies += str(base_freq) + " "
    print base_index_map[line_index] + ": " + frequencies.strip()