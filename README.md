# genotyping_method
### Accurate genotype-level identification of enteroviruses and adenoviruses.

This next-generation sequencing (NGS) virus identification method uses only the highly variable P1 capsid region of enteroviruses and the the hexon capsid gene of the adenoviruses as references for identification.

##### System requirements
- UNIX-based system
- BWA aligner
- Python 3.0 or above
- Perl
- samtools

##### Creating and updating a database of variable regions
1. Use this Python script to create a file of perl commands that will search GenBank for all available enterovirus or adenovirus genomes. This scpirt writes perl commands into a .sh file: make_perl_commands.py 
2. Run the created .sh file which will produce fasta files of all the genomes.
3. Add genotypes names as prefix to each fasta header: rename_fasta_headers.py
4. Concatenate all fasta files.

##### NGS alignment for identification
1. Python script that writes bwa alignment commands into a .sh file: write_bwa_commands.py. Usage: write_bwa_commands.py R1.fasta R2.fasta refs.fasta 
2. Run the created .sh file which will align reads from the sample to all references.
3. Count the number of alignments to each reference sequence and write them to a csv file: count_ref_V4.py

