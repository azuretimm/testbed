import os, sys
print(os.getcwd())
fw = open('out.fasta', 'w')
for files in os.listdir():
    if "txt" in files:
        fr = open(files, 'r')
        sequence = fr.readline()
        fw.seek(0, 2)
        fw.write('>'+files+"\n")
        fw.write(sequence+"\n")
        fr.close()
fw.close()