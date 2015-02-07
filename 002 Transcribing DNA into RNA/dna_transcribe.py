from sys import argv
script, filename = argv

file = open(filename)
DNA = file.read()
file.close()

# replace all 'C' with 'U'
RNA = DNA
RNA = RNA.replace("T", "U")

print RNA
