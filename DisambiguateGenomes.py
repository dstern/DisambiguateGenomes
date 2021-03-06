#!/usr/bin/env python

import os,sys
import getopt
import numpy as np
from pyfasta import Fasta

def main():
        
        #parse command line options
        try:
                opts, arg = getopt.getopt(sys.argv[1:],"h", ["help"])
        except getopt.error, msg:
                print msg
                print "for help use --help"
                sys.exit(2)
        # process options
        for o, a in opts:
                if o in ("-h", "--help"):
                        print __doc__
                        sys.exit(0)
        if len(arg) < 3:
                print "\nUsage: python CompareGenomes.py <Genome1> <Genome2> <GenomeOut>\m"                
                sys.exit(0)
        #process arguments

        genome1 = arg[0]
        genome2 = arg[1]
        genomeOut = arg[2]

        #open genomeOut file to write new genome
        gOut = open(genomeOut,'w')
        
        #open both genomes as pyFasta arrays
        Fgenome1 = Fasta(genome1)
        Fgenome2 = Fasta(genome2)
        
        #get chromosome names
        chroms = Fgenome1.keys()
        
        #for each chromosome
        
        for chrom in chroms:
        
                #convert pyFasta arrays to numpy arrays
                
                np_genome1 = np.array(Fgenome1[chrom])
                np_genome2 = np.array(Fgenome2[chrom])
                
                #get Boolean array from elementwise comparison of chromosomes
                chrom_matches = np.core.defchararray.equal(np_genome1,np_genome2)
                
                #make new array of size of chrom, fill with N's
                
                out_genome = np.chararray(len(np_genome1))
                out_genome[:] = 'N'
                
                #fill matching positions
                
                out_genome[chrom_matches] = np_genome1[chrom_matches]
                
                #write this chrom as new lines in open file
                
                gOut.write('>' + str(chrom) + '\n')
                gOut.write(out_genome.tostring() + '\n')
                
        gOut.close()

if __name__ == "__main__":
        sys.exit(main())
