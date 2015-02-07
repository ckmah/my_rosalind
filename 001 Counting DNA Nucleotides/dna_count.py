from array import *
from sys import argv
# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# base_count = array('i', [0, 0, 0, 0])

# input = open("rosalind_dna.txt")
# DNA = input.read()
# input.close()
# for nuc in DNA:
#     if nuc == 'A':
#         base_count[0] += 1
#     elif nuc == 'C':
#         base_count[1] += 1
#     elif nuc == 'G':
#         base_count[2] += 1
#     elif nuc == 'T':
#         base_count[3] += 1

# output = ""
# for base in base_count:
#     output += str(base) + " "
# print output

#alternative solution
script, filename = argv
input = open( filename )
DNA = input.read()
input.close()
print DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")
