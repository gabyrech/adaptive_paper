#!/usr/bin/python
# This script takes the VCF file from DGRPv2 and transform it to the SNP format requiered by iHSComputer.
import sys

vcf = open(sys.argv[1]).readlines()
samples = int(sys.argv[2])

chrom = ["2L", "2R", "3L", "3R", "4", "X"]

for c in chrom:
	snpFile = open("chr"+str(c)+"SNPS.csv", "w")
	for line in vcf:
		if str(c) == line.split("\t")[0]:
			hap = []
			pos = line.split("\t")[1]
			ref = line.split("\t")[3]
			alt = line.split("\t")[4]
			genotypes = line.split("\t")[-samples:]
			for sample in genotypes:
				if sample == "0/0" or sample == "0/0\n":
					allele = ref
				elif sample == "1/1" or sample == "1/1\n":
					allele = alt
				else:
					allele = "N"
				hap.append(allele)
			print >> snpFile, pos + "," + "".join(hap)
