# -*- coding: utf-8 -*-
"""
Count the number of alignments to each reference.
Align fastq files of sample to a fastq of references.
Sort and index bam file before running this script.
"""
import sys
import pysam
import operator
import csv

# make dictionary {reference_name:alignment counts}, sysarg is bam file
def get_dict(sysarg):
    sample_name = "_".join(sysarg.split("_")[0:3])
    count_file=open(sample_name+"_counts.csv", "w")
    count_file.write("reference,count\n")
    samfile = pysam.AlignmentFile(sysarg, "rb") # import bam
    refs = samfile.references
    sum_dict = {} # {serotype:alignments}
    ref_dict = {} # {ref_name:alignments}
    for ref in refs: # a ref is an accession name
        ref_dict[ref] = samfile.count(reference=ref)
        sero = ref.split("_")[0]
        sum_dict.setdefault(sero,[]).append(samfile.count(reference=ref))
    for sero in sum_dict:
       sum_dict[sero] = sum(sum_dict[sero]) # sum of alignments per serotype
    sorted_acc=sorted(ref_dict.items(), key=operator.itemgetter(1), reverse=True) # list of tuples (ref, counts)
    obj=csv.writer(count_file)
    for acc in sorted_acc:
        obj.writerow(acc) # write ref,counts
    count_file.close()
    sorted_sum_dict = sorted(sum_dict.items(), key=operator.itemgetter(1), reverse=True) # list of tuples
    geno_file=open(sample_name+"_geno_counts.csv", "w")
    geno_file.write("genotype,count\n")
    obj2=csv.writer(geno_file)
    for geno in sorted_sum_dict:
        obj2.writerow(geno)
    geno_file.close()

p1 = get_dict(sys.argv[1]) # bam files
full = get_dict(sys.argv[2])

#top_3 = sorted(ref_dict, key=ref_dict.get, reverse=True)[:3]
#for ref in top_3:
#   print(ref+str(ref_dict[ref]))

#barWidth = 0.25
#r1 = np.arange(len(p1[0]))
#r2 = [x + barWidth for x in r1]
#plt.bar(r1, p1[1], align='center', linewidth=0, width=barWidth, edgecolor='white', color="skyblue")
#plt.bar(r2, full[1], align='center', linewidth=0, width=barWidth, edgecolor='white', color="pink")
## plt.xticks(range(len(sorted_sum_dict)), list(sorted_sum_dict.keys()))
#plt.ylabel('Number of aligned reads')
#plt.xlabel('Serotype')
#plt.title(sample_name)
#plt.show()

