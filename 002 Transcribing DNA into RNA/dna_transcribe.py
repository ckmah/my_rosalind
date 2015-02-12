# !/usr/bin/env python
# author: Clarence Mah
# Print the RNA transcription of a given DNA sequence in a text file.

from sys import argv
script, filename = argv

file = open(filename)
DNA = file.read()
file.close()

# replace all 'C' with 'U'
RNA = DNA
RNA = RNA.replace("T", "U")

print RNA
