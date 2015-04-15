# !/usr/bin/env python
# author: Clarence Mah
# Given: A collection of k (k<=100) DNA strings of length at most 1 kbp
# each in FASTA format.
# Return: A longest common sub_seqing of the collection. (If multiple
# solutions exist, you may return any single solution.)
from sys import argv

script, filename = argv
f = open(filename)
data = [line.strip() for line in f.readlines()]
seqs = []
for index in range(1, len(data), 2):
    seqs.append(data[index])
f.close()


def lcs(seqs):
    '''
    Finds the longest common sequence in a set of sequences.
    '''
    short_seq = min(seqs, key=len)
    # sub sequence left bound
    for seq_size in range(len(short_seq), 0, -1):
        # sub sequence right bound
        for start in range(len(short_seq) - seq_size + 1):
            sub_seq = short_seq[start:start + seq_size]

            # find common sub seqence, break if can't find
            found = True
            for seq in seqs:
                if sub_seq not in seq:
                    found = False
                    break
            # found common sub seqence in all sequences
            if found:
                return sub_seq
    return ""

print lcs(seqs)
