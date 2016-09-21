#!/usr/bin/python
# This script takes the VCF file from DGRPv2 and transform it to the SNP format requiered by iHSComputer.
import sys

vcf = open(sys.argv[1]).readlines()
