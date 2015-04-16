# DisambiguateGenomes
A Python script to convert polymorphic sites into Ns between two genomes of identical length. 

Dependencies: os, sys, getopt, numpy, pyfasta

Important notes: 
1 - Two genomes must be identical lengths. Ideally, they are two genomes updated using Genome Updating script of MSG.
2 - The disambiguated genome can be disambiguated sequentially with multiple genomes. This is good way to reduce species polymorphism from a genome. These genomes provide cleaner results in the MSG pipeline
