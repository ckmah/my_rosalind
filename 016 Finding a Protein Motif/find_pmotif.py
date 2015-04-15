from sys import argv
import urllib2
import re
import StringIO

script, pfile, pmotif = argv
# protein ids
f = open(pfile)
p_ids = f.readlines()
f.close()

# target protein motif
f = open(pmotif)
pattern = f.readline()
f.close()

# regex translation
pattern = re.sub(r"{", "[^", pattern)
pattern = re.sub(r"}", "]", pattern)
pattern = "(?=(" + pattern + "))"  # allows for overlapping matches
pattern = re.compile(pattern)

protein_url = "http://www.uniprot.org/uniprot/"
txt_prefix = ".txt"
fasta_prefix = ".fasta"

pseqs = {}

# parse all protein sequences
for entry in p_ids:
    # grab protein database entry
    url = protein_url + entry.strip() + txt_prefix
    response = urllib2.urlopen(url)
    contents = response.read()
    contents_buf = StringIO.StringIO(contents)

    # grab sequence data
    line = contents_buf.readline()
    while len(line) > 0:
        if line.startswith("SQ"):
            pseqs[entry] = contents_buf.read()
            break

        line = contents_buf.readline()

    # format sequence data
    cur_seq = pseqs[entry]
    cur_seq = cur_seq[:cur_seq.rfind('\\\\\n')]
    cur_seq = cur_seq[:cur_seq.rfind('\n')]
    cur_seq = re.sub(r"[\n\t ]", "", cur_seq)

    positions = ""
    for m in re.finditer(pattern, cur_seq):
        positions += str(m.start(0) + 1) + " "

    if len(positions) > 0:
        print entry.strip()
        print positions.strip()
