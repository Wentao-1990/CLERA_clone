# CLERA_clone

## Here is a script to extracted DNA sequences and quality data from the ab1 files generated from Sanger sequencing.

### Prerequiest: 
  biopython==1.80 #using pip install
### Description
The code is designed to identify sequences with lengths exceeding 500 base pairs. By modifying the length parameter, the code will search for sequences that meet the new criterion. As the initial step, the code encodes the sequences into a binary format, where '1' indicates a base quality above 35, and '0' denotes otherwise. Subsequently, the code seeks sequences that surpass the 500-base pair threshold and subsequently reports their identification. If there are no sequences present on the right side, it is likely due to low-quality data in that region.
