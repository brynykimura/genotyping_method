# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:04:24 2019
SUMMARY: makes sh file of perl commands for searching GenBank.
@author: bk426408
"""
import sys
# SUMMARY: write sh file to run perl script to search GenBank and return fasta files.
#import os

#os.chdir("C:/Users/bk426408/Documents/Sami_P1/sami_scripts/")

geno_short=["CVA2","CVA3","CVA4","CVA5","CVA6","CVA7","CVA8","CVA10","CVA12","CVA14","CVA16",
"EVA71","EVA76","EVA89","EVA90","EVA91","EVA92","EVA114","EVA119","EVA120","EVA121",
"CVB1","CVB2","CVB3","CVB4","CVB5","CVB6","CVA9","echo1","echo2","echo3","echo4","echo5","echo6",
"echo7","echo9","echo11","echo12","echo13","echo14","echo15","echo16","echo17","echo18","echo19","echo20",
"echo21","echo24","echo25","echo26","echo27","echo29","echo30","echo31","echo32","echo33","EVB69","EVB73",
"EVB74","EVB75","EVB77","EVB78","EVB79","EVB80","EVB81","EVB82","EVB83","EVB84","EVB85",
"EVB86","EVB87","EVB88","EVB93","EVB97","EVB98","EVB100","EVB101","EVB106","EVB107",
"PV1","PV2","PV3","CVA1","CVA11","CVA13","CVA17","CVA19","CVA20","CVA21","CVA22","CVA24",
"EVC95","EVC96","EVC99","EVC102","EVC104","EVC105","EVC109","EVC113","EVC116","EVC117",
"EVC118","EVD68","EVD70","EVD94","EVD111"]

geno_long=["coxsackievirus A2","coxsackievirus A3","coxsackievirus A4","coxsackievirus A5",
"coxsackievirus A6","coxsackievirus A7","coxsackievirus A8","coxsackievirus A10",
"coxsackievirus A12","coxsackievirus A14","coxsackievirus A16","enterovirus A71",
"enterovirus A76","enterovirus A89","enterovirus A90","enterovirus A91","enterovirus A92",
"enterovirus A114","enterovirus A119","enterovirus A120","enterovirus A121",
"coxsackievirus B1","coxsackievirus B2","coxsackievirus B3","coxsackievirus B4",
"coxsackievirus B5","coxsackievirus B6","coxsackievirus A9","echovirus 1","echovirus 2",
"echovirus 3"," echovirus 4","echovirus 5","echovirus 6","echovirus 7","echovirus 9",
"echovirus 11","echovirus 12","echovirus 13","echovirus 14","echovirus 15","echovirus 16",
"echovirus 17","echovirus 18","echovirus 19","echovirus 20","echovirus 21","echovirus 24",
"echovirus 25","echovirus 26","echovirus 27","echovirus 29","echovirus 30","echovirus 31",
"echovirus 32","echovirus 33","enterovirus B69","enterovirus B73","enterovirus B74",
"enterovirus B75","enterovirus B77","enterovirus B78","enterovirus B79","enterovirus B80",
"enterovirus B81","enterovirus B82","enterovirus B83","enterovirus B84","enterovirus B85",
"enterovirus B86","enterovirus B87","enterovirus B88","enterovirus B93","enterovirus B97",
"enterovirus B98","enterovirus B100","enterovirus B101","enterovirus B106","enterovirus B107",
"human poliovirus 1","human poliovirus 2","human poliovirus 3","coxsackievirus A1",
"coxsackievirus A11","coxsackievirus A13","coxsackievirus A17","coxsackievirus A19",
"coxsackievirus A20","coxsackievirus A21","coxsackievirus A22","coxsackievirus A24",
"enterovirus C95","enterovirus C96","enterovirus C99","enterovirus C102","enterovirus C104",
"enterovirus C105","enterovirus C109","enterovirus C113","enterovirus C116","enterovirus C117",
"enterovirus C118","enterovirus D68","enterovirus D70","enterovirus D94","enterovirus D111"]

long_short=list(zip(geno_short, geno_long))
# sys.argv[2] is the perl script that gives the correct output: 
# search_db_codingNT.pl, search_db_codingAA.pl, search_db_fullNT.pl 
perl_script=sys.argv[2]
# sys.argv[1] what you want to name the file, name of dir where fastas will go
filename="search_list_"+sys.argv[1]+".sh"
sh_file=open(filename, "w")

for geno in long_short:
    sh_file.write("perl /homeappl/home/kimurabr/scripts/P1_tool/"+perl_script+" \"" + geno[1] +
                  "\" > /wrk/kimurabr/P1_align/"+sys.argv[1]+"/" + geno[0] + ".fasta\n")

sh_file.close()
