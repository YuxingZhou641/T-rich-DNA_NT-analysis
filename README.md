# T-rich-DNA_NT analysis
This section provides customized code for the analysis presented in the paper: Molecular Basis of an Adenine-Rich Template DNA-Induced Spontaneous Transcription Termination.

## Software/package
1. Python -v3.9.12 
2. argparse -v3.2

## Calculate the T Enrichment Score
To calculate the T enrichment score, use base_enrichment.py with the following command:
```
python base_enrichment.py --genome {your_genome.fa} --output {your_output_file_name} --window {default=10, your expected window size} --base {default=T, base to calculate}
```
This command generates a BED file containing the base enrichment information. You can convert the resulting BED file to a BigWig file for visualization using bedGraphToBigWig.

T-scores were calculated using the TAIR10 genomic sequence. For a given position k
in the genome, the T-score was calculated based on the base composition of the
sequence from position k-3 to k+3. Over this 7-bp region, the score was
calculated as the number of thymines within the region, plus a bonus score for
consecutive thymines, and a penalty for consecutive non- thymines. If the score was
negative it was set to zero. Specifically, given a position k in the genome, t equal to the
number of thymines in the region of k-3 to k+3, c equal to the number of runs of
consecutive thymines, xi as the length of the ith run of consecutive thymines in the
region of k-3 to k+3, and g equal to the longest run of consecutive non- thymines in the
region of k-3 to k+3, the score was calculated as:

$T_score = \max (t+(\sum^(c)_i=1+\sum^(x_i)-1)_j=1-g,0)
