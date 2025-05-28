# Noncoding de novo mutations in SCN2A are associated with autism spectrum disorders

# Installation
We recommend using Conda to set up the environment. If Conda is not installed, run the following commands in Linux to install it.
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Install Bcftools
We recommend using Conda to install Bcftools.

### Install ANNOVAR
Typically you will go to the [ANNOVAR website](https://annovar.openbioinformatics.org/en/latest/), fill in a registration form, and download the package there. When you have requested the ANNOVAR from the website and downloaded it, you will receive a compressed file ```annovar.latest.tar.gz```, you will need to unzip it. Then follow the user guide to install ANNOVAR.


# Inference

## Step 1: Generate family trio vcf files

``` bcftools merge $patient_id.gvcf.gz $parentA.gvcf.gz $parentB.gvcf.gz -g path/to/Homo_sapiens_assembly38.fasta -O v -o $patient_id.trio.gvcf.gz ```

## Step 2: Extract de novo variants

```
python Generate de_novo_extract.py
```

## Step 3: 




