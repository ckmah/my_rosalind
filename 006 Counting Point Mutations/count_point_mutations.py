from sys import argv

script, filename = argv

file = open(filename)
lines = file.read().split('\n')
file.close()

control = lines[0]
exp = lines[1]

# tracks # of point mutations found
count = 0

for a, b in zip(control, exp):
    if (a != b):
        count = count + 1

print count