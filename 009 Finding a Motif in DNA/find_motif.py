# !/usr/bin/env python
# # author: Clarence Mah
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

from sys import argv
import string

script, filename = argv

# read in dna and motif
f = open(filename)
dnaseq = f.readline().strip()
motif = f.readline().strip()
f.close()

motif_locations = []

index = 0
# loop through DNA sequence
while index < len(dnaseq):
    # save index of first occurence of motif in dnaseq substring
    found_index = string.find(dnaseq[index:], motif)

    # add absolute string index, 1-based numbering
    if found_index != -1:
        abs_index = index + found_index + 1
        if abs_index not in motif_locations:
            motif_locations.append(abs_index)
        # print "found_index = " + str(index + found_index + 1)
    else:
        break

    # start looking past found_index
    index += 1


# format result before printing
result = ""
for location in motif_locations:
    result += str(location) + " "

print result.strip()