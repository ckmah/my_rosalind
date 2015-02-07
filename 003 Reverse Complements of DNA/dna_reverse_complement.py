from sys import argv

script, filename = argv

file = open(filename)
DNA = file.read()
file.close()

complements = {"A": "T", "C": "G", "T": "A", "G": "C"}
DNA_complement = ""

# reverse DNA sequence and replace with complement
for base in DNA:
    if base in complements.keys():
        DNA_complement = complements[base] + DNA_complement

print DNA_complement
