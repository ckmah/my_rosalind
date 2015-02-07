from sys import argv

script, filename = argv

file = open(filename)
lines = file.read().split('\n')
file.close()

# if line contains '>' then count GC content in next line
# save gc content percentage to ID number as variable

ids = []
seqs = []

# separate header/sequence lines
for line in lines:
    if '>' in line:
        ids.append(line)
    else:
        seqs.append(line)

# id of sequence with highest GC content
id_final = ""
# GC content value
GC_final = 0

# compare each set of ID/sequences
for id, seq in zip(ids, seqs):
    GC_content = 100.*(seq.count("G") + seq.count("C"))/len(seq)
    if GC_content > GC_final:
        GC_final = GC_content
        id_final = id[1:]

print id_final
print GC_final