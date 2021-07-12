# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:45:05 2019

Arguments: R1,R2, references fasta

Requires bwa, samtools

needs to write these to sh file:

#NGSV2 P1 alignment:
bwa mem -t 3 /wrk/kimurabr/P1_align/ref/P1_nt_V2.fasta NGSV2_trimmed_R1_L001.fastq.gz 
NGSV2_trimmed_R2_L001.fastq.gz > /wrk/kimurabr/P1_align/NGSV2/all_seqsNGSV2_P1.sam

#Filter low mapq:
samtools view -bq 10 all_seqsNGSV2_P1.sam > NGSV2_all_mapq.bam

#sort bam:
samtools sort -o NGSV2_all_P1_mapq_sort.bam NGSV2_all_mapq.bam

#index bam:
samtools index NGSV2_all_P1_mapq_sort.bam

@author: bk426408
"""
import sys

R1 = "/wrk/kimurabr/DONOTREMOVE/fastqs/"+sys.argv[1]
R2 = "/wrk/kimurabr/DONOTREMOVE/fastqs/"+sys.argv[2]
sample_name = sys.argv[1].split("_")[0]
references = "/wrk/kimurabr/P1_align/ref/"+sys.argv[3].split(".")[0]
references_no_fa=references.split("/")[-1].split(".")[0]

sh_filename=sample_name+"_"+references_no_fa+"_bwa_samtools.sh"
sh_file=open(sh_filename, "w")

sh_file.write("echo bwa "+sample_name+"\n")
sh_file.write("bwa mem -t 3 "+references+" "+R1+" "+R2+" > /wrk/kimurabr/P1_align/"
              +sample_name+"/"+sample_name+"_"+references_no_fa+".sam\n\n")

sh_file.write("echo filter mapq "+sample_name+"\n")
sh_file.write("samtools view -bq 10 "+sample_name+"_"+references_no_fa+".sam > "
              +sample_name+"_"+references_no_fa+"_mapq.bam\n\n")

sh_file.write("echo sort "+sample_name+"\n")
sh_file.write("samtools sort -o "+sample_name+"_"+references_no_fa+"_sorted_mapq.bam "
              +sample_name+"_"+references_no_fa+"_mapq.bam\n\n")

sh_file.write("echo index "+sample_name+"\n")
sh_file.write("samtools index "+sample_name+"_"+references_no_fa+"_sorted_mapq.bam\n\n")

sh_file.write("echo rm "+sample_name+"\n")
sh_file.write("rm -f "+sample_name+"_"+references_no_fa+".sam "+sample_name
              +"_"+references_no_fa+"_mapq.bam\n\n")

sh_file.write("#---------------")

sh_file.close()