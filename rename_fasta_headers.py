# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:24:05 2019

Summary: Add prefixes to fasta headers based on file names. Anything before 
first underscore in the filename is added to headers of sequences.

@author: User
"""
import os
from Bio import SeqIO
import sys
#from Bio.Alphabet import IUPAC

#os.chdir("C:/Users/bk426408/Documents/Sami_P1/Reference_Sequences/Full_Length_References_V2/")

# directory = "C:/Users/bk426408/Documents/Sami_P1/Reference_Sequences/Full_Length_References_V2/"

directory = sys.argv[1] # directory of no-prefix-fastas

# add prefix to fasta headers (https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for filename in files:
    with open(filename) as original:
        sero=filename.rsplit(".",1)[0]
        print(sero)
        #corrected_file = "C:/Users/bk426408/Documents/Sami_P1/Reference_Sequences/prefix_V2/"+sero+"_prefix.fasta"
        corrected_file = directory+"/prefix/"+sero+"_prefix.fasta"
        with open(corrected_file, 'w') as corrected:
            records = SeqIO.parse(filename, 'fasta') 
            for record in records: # headers
                print(record.id)
                #print(record.id.split("|")[1])
                add_sero=sero+"_"+record.id
                print(add_sero)
                record.id = add_sero
                #record.description = add_sero
                SeqIO.write(record, corrected, 'fasta')

# below code is for if there is a bar (|) in the headers
## add prefix to fasta headers
#for filename in os.listdir(directory):
#    with open(filename) as original:
#        sero=filename.rsplit("_",1)[0]
#        print(sero)
#        corrected_file = "C:/Users/bk426408/Documents/Sami_P1/Reference_Sequences/prefix_V2/"+sero+"_prefix.fasta"
#        with open(corrected_file, 'w') as corrected:
#            records = SeqIO.parse(filename, 'fasta') 
#            for record in records: # headers
#                print(record.id)
#                print(record.id.split("|")[1])
#                add_sero=sero+"_"+record.id.split("|")[1]
#                print(add_sero)
#                record.id = add_sero
#                record.description = add_sero
#                SeqIO.write(record, corrected, 'fasta')
            
# count how many sequences for each serotype
counter=0
for filename in os.listdir(directory):
    counter=0
    print(filename)
    with open(filename) as original:
        records = SeqIO.parse(filename, 'fasta')
        for record in records:
            counter+=1
    print(counter)