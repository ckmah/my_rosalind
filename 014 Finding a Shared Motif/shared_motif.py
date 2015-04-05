# !/usr/bin/env python
# author: Clarence Mah
# Given: A collection of k (k<=100) DNA strings of length at most 1 kbp
# each in FASTA format.
# Return: A longest common substring of the collection. (If multiple
# solutions exist, you may return any single solution.)
from sys import argv

script, filename = argv
f = open(filename)
data = [line.strip() for line in f.readlines()]
f.close()

# create dict of {id: sequence}
id_seq = {}
iter_data = iter(data)
for line in iter_data:
    id_seq[line] = next(iter_data)

# retrieve shortest sequence
short = ""
for k in id_seq:
    if short == "":
        short = id_seq[k]
    else:
        seq = id_seq[k]
        if len(short) > len(seq):
            short = seq
            
def is_substr(str1, str2):
    '''
    Checks if str1 is substring of str2.
    '''
    for i in range(0, len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]:
            return True
    return False


def longer_string(str1, str2):
    '''
    Returns the longer of the two strings.
    '''
    if len(str1) > len(str2):
        return str1
    else:
        return str2


def lcs_list(short, strings):
    '''
    Returns the longest common substring in the list of strings.
    '''
    max_count = 0
    lcs = ''

    # loop through start indices
    for index in range(0, len(short)):
        # loop through end indices per start index
        for end_index in reversed(range(index + 1, len(short)+1)):
            # loop through each string
            max_count = 0
            for k in strings:
                # return short if all have substring
                if is_substr(short[index:end_index], strings[k]):
                    max_count += 1
                    if max_count == len(strings) and len(short[index:end_index]) > len(lcs):
                        lcs = short[index:end_index]
                else:
                    break

    return lcs

print lcs_list(short, id_seq)
