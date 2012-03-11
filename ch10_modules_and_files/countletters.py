#
# countletters.py
#

from sys import argv

def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)

infile_name = argv[1]
outfile_name = argv[2]

infile = open(infile_name, 'r')
text = infile.read()
infile.close()

counts = 128 * [0]

for letter in text:
    counts[ord(letter)] += 1

outfile = open(outfile_name, 'w')
outfile.write("%-12s%s" % ("Character", "Count"))
outfile.write("===============\n")

for i in range(len(counts)):
    if counts[i]:
        outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()

