# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:32:14 2019
SUMMARY: finds end of P1 from nt coding sequences and cuts them so it’s only 
P1 region (run locally).
Count how many occurrances of a string of amino acids are in a 
sequence. Show the positions of the string found in each sequence. Count how 
many times a set of strings appear together in the same sequence.
@author: Bryn Kimura
"""

from Bio import SeqIO
#from Bio.Alphabet import IUPAC
#from contig_to_aa_V2 import seq2AA
#from Bio import AlignIO
from collections import Counter # input list, returns a dictionary of counts of elements
import os
os.chdir("C:/Users/bk426408/Documents/Sami_P1/reference_sequences/")

P2A_starts = ["GRFG", "GKLG", "GEFG", "GKCG", "GVFG", "GAFG", "GFGH", "GRLG", 
             "GYGH", "GHGH", "GLGH", "GTFG", "GAFE", "GGFG", "GKFG",
             "GPYQ", "GAFQ", "GAFG", "GVVG", "GPYG"]
VP1_end = ["LTTY"]
CVB4_P2A_starts = ["GHQS", "GQQS", "GQQT", "GQQA"]
CVB2_5_P2A_starts = ["GAYGQQ",  "GAYGQQ", "GAFGHQ", "GTYGQQ", "GTRGQQ", "GVFGQQ",
                     "GAFGQQ",]

# make dictionary of fasta headers (keys) and nucleotide positions for end of VP1 (values)
# also write document: header, VP1 AA end position, P2A start AAs
def dict_write(mer):
    fasta_dict[ID]=(j)*3
    end_pos_file.write("> " + consensus.id + "\n")
    end_pos_file.write(str(j) + "\n")
    end_pos_file.write(mer + "\n")

# when start of P2A is found, save nucleotide position of end of VP1 in dict.
end_pos_file=open("end_pos.fasta", "w") 
fasta_dict={}
aa = ["CVB2", "CVB5"]
for consensus in SeqIO.parse("aa_seqs.fasta", "fasta"):
    seq_str = str(consensus.seq)
    ID = consensus.id.split("_")[0]
    for j in range(0, len(seq_str)):
        four_mer = seq_str[j:j+4]
        six_mer = seq_str[j:j+6]
        if any(x in ID for x in aa):
            if six_mer in CVB2_5_P2A_starts and j > 815:
                dict_write(six_mer)
                break
        if "CVB4" in ID:
            if four_mer in CVB4_P2A_starts and j > 810:
                dict_write(four_mer)
                break
        if four_mer in P2A_starts and j > 810:
            dict_write(four_mer)
            break
        if four_mer in VP1_end and j > 810:
            dict_write(four_mer)
            break
end_pos_file.close()

# put nucleotide sequences of just P1 in a file
fail_file=open("no_vp1_end.fasta", "w")                      
P1_file=open("P1_nt.fasta", "w")              
counter=0
for consensus in SeqIO.parse("coding_nt.fasta", "fasta"):
    seq_str = str(consensus.seq)
    try:
        fasta_dict[consensus.id.split("_")[0]]
        P1_file.write("> " + consensus.id + "\n")
        P1_file.write(seq_str[:fasta_dict[consensus.id.split("_")[0]]] + "\n")
    except KeyError:
        counter += 1 
        fail_file.write("> " + consensus.id + "\n")
P1_file.close()
fail_file.close()

#counter
#Out[69]: 105

# count number of times substring occurs above 820
def occurances(substring):
    counts=[]
    for consensus in SeqIO.parse("all_seros_AA.fasta", "fasta"):
        seq_str = str(consensus.seq)[820:]
        if substring in seq_str:
            counts.append(seq_str.count(substring))
    print(substring)
    return(Counter(counts)) # dictionary

occurances("GKFG")

single_sums=[]
for start in P2A_starts:
    single_sum=occurances(start) # dictionary
    print(single_sum)
    single_sums.append(single_sum[1])
print(sum(single_sums)) # sum of all endings: 3054/3654

# count how many sequences end with LTTY
i=0
j=0
for consensus in SeqIO.parse("all_seros_AA.fasta", "fasta"):
    j+=1
    seq_str = str(consensus.seq)
    seq_noDash=seq_str.replace("-","")
    if seq_noDash.endswith("LTTY"):
        i+=1
i # 489 + 3054 = 3543/3654
j # 3654

counts=[]
a=["GKFG", "GAFG", "GVFG"] 
for consensus in SeqIO.parse("all_seros_AA.fasta", "fasta"):
    seq_str = str(consensus.seq)
    matches = [x for x in a if x in seq_str]
    print(matches)
    counts.append(tuple(matches))

freq = Counter(counts)

print(freq[('GAFG', 'GVFG')]) #14
print(freq[('GKFG', 'GVFG')]) #1520
print(freq[('GKFG', 'GAFG')]) #0
print(freq[('GVFG',)]) #187
print(freq[('GKFG',)]) #14
print(freq[('GAFG',)]) #353




