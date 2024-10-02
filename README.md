# T-enrich-analysis
Here is the customized code for paper Molecular basis of an adenine-rich template DNA-induced spontaneous transcription termination

Calculate the T enrichment score using base_enrichment.py using following command
```
python base_enrichment.py --genome {your_genoem.fa} --output {your output file name} --window {default = 10, your expect window size} --base {default = T, base to calculate}
```
This step will generate a bed file containing the Base enrichment info then you may convert this bed file to bigwig filr for visualization using BedgraghToBigwig.
