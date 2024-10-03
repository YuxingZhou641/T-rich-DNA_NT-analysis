# T-enrich-analysis
Here is the customized code for paper Molecular basis of an adenine-rich template DNA-induced spontaneous transcription termination

Calculate the T enrichment score using base_enrichment.py using following command
```
python base_enrichment.py --genome {your_genoem.fa} --output {your output file name} --window {default = 10, your expect window size} --base {default = T, base to calculate}
```
This step will generate a bed file containing the Base enrichment info then you may convert this bed file to bigwig filr for visualization using BedgraghToBigwig.

# T boundaries detection
You may detect the certain base enriched boundaries for a given region using boundary_detection.py and the bed file generate by base_enrichment.py.
```
python boundary_detection.py --region {your region in BED format} --output {your output file name} --ref {Bed file generate by base_enrichment.py} --window {default = 30, your expect window size for boundaries} --filter {default = 10, lowest score to be consider as a enrichment}
```
This step will generate a bed file containing a seperate column with True/False to mark wether a region has certain base enriched boudaries or not.
