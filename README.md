# Noncoding de novo mutations in SCN2A are associated with autism spectrum disorders

# Installation
We recommend using Conda to set up the environment. If Conda is not installed, run the following commands in Linux to install it.
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
### a) Install Bcftools
We recommend using Conda to install Bcftools.

### b) Install ANNOVAR
Typically you will go to the [ANNOVAR website](https://annovar.openbioinformatics.org/en/latest/), fill in a registration form, and download the package there. When you have requested the ANNOVAR from the website and downloaded it, you will receive a compressed file ```annovar.latest.tar.gz```, you will need to unzip it. Then follow the user guide to install ANNOVAR.

# Inference

### Step 1: Generate family trio vcf files

``` 
bcftools merge $patient_id.gvcf.gz $parentA.gvcf.gz $parentB.gvcf.gz -g path/to/Homo_sapiens_assembly38.fasta -O v -o $patient_id.trio.gvcf.gz
```

### Step 2: Extract de novo variants and then do filter (e.g. GQ, AD, and DP)

``` 
python Generate de_novo_extract.py

python de_novo_filter.py
```

### Step 3. Run ANNOVAR to filter de novo mutations
Input files to ANNOVAR refer to VCF file

```
perl table_annovar.pl patient_id.de.novo.vcf.gz humandb/ -buildver hg38 -out myanno.patient_id -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp47a,gnomad312_exome,gnomad312_genome,clinvar_20240917 -operation gx,r,f,f,f,f,f,f -nastring . -vcfinput -polish
```

### Step 4: Use allele frequency cut off to filter variants (Gnomad <1x10-3)
```
bcftools view myanno.patient_id.de.novo.vcf |sed 's/\.;ANNOVAR_DATE/ANNOVAR_DATE/g'| bcftools annotate -x "ID" --set-id +'%CHROM\_%POS\_%REF\_%FIRST_ALT'|sed '/^##INFO=<ID=gnomad312/ s/Type=String/Type=Float/'|bcftools view -i 'INFO/gnomad312_AF=="." || INFO/gnomad312_AF<=0.001' |bgzip > path/to/patient_id.de.novo.gnomad.vcf.gz
```
### Step 5: Point-based test
the input is the detected de novo mutations, it look like this:
```
chr     pos     ID      sample  gene    Func    ExonicFunc      cadd_score
chr10   100001412       chr10_100001412_T_G     SP0154098       DNMBP   intronic        .       2.322
chr10   100029096       chr10_100029096_C_T     SP0334963       DNMBP\x3bCPN1   intergenic      .       2.21
chr10   100035234       chr10_100035234_TA_T    SP0143622       DNMBP\x3bCPN1   intergenic      .       1.547
chr10   100037988       chr10_100037988_C_T     SP0276261       DNMBP\x3bCPN1   intergenic      .       4.346
chr10   100040361       chr10_100040361_GA_G    SP0129400       DNMBP\x3bCPN1   intergenic      .       2.681
chr10   100046733       chr10_100046733_A_AC    SP0157054       CPN1    intronic        .       0.889
```
After runing ```Expected_denovo_calculated_Fisher_test.ipynb```, you can get the p value for point-based test

### Step 6: Segment-based test
The Gnocchi score file ```constraint_z_genome_1kb.qc.download.txt.gz``` can be downloaded from the [Chen et al.](https://www.nature.com/articles/s41586-023-06045-0) paper

the input is the detected de novo mutations, it look like this:
```
chr     pos     ID      sample  gene    Func    ExonicFunc      cadd_score
chr10   100001412       chr10_100001412_T_G     SP0154098       DNMBP   intronic        .       2.322
chr10   100029096       chr10_100029096_C_T     SP0334963       DNMBP\x3bCPN1   intergenic      .       2.21
chr10   100035234       chr10_100035234_TA_T    SP0143622       DNMBP\x3bCPN1   intergenic      .       1.547
chr10   100037988       chr10_100037988_C_T     SP0276261       DNMBP\x3bCPN1   intergenic      .       4.346
chr10   100040361       chr10_100040361_GA_G    SP0129400       DNMBP\x3bCPN1   intergenic      .       2.681
chr10   100046733       chr10_100046733_A_AC    SP0157054       CPN1    intronic        .       0.889
```
After runing ```segmet_based_test.ipynb```, you can get the p value for segment-based test




