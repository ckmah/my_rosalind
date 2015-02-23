# !/usr/bin/env python
# author: Clarence Mah

from sys import argv

script, filename, k_overlap = argv

f = open(filename)
data = [line.strip() for line in f.readlines()]
f.close()

# create map of id to sequence
id_seq = {}
iter_data = iter(data)
for line in iter_data:
    id_seq[line] = next(iter_data)

edges = []

# find suffix to prefix matches excluding self match
for k1 in id_seq:
    for k2 in id_seq:
        if id_seq[k1][-3:] == id_seq[k2][:3] and k1 != k2:
            edges.append(tuple([k1, k2]))

# print edges formatted
for edge in edges:
    print edge[0].strip('>'), edge[1].strip('>')