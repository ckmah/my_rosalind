# !/usr/bin/env python
# author: Clarence Mah
# description: Return 4 integers separated by spaces counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' in given text file.

from array import *
from sys import argv

script, filename = argv
input = open( filename )
DNA = input.read()
input.close()
print DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")
