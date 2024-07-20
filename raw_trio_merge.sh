#!/bin/bash

#SBATCH --time=12:00:00
#SBATCH --array=1-5697    # create n tasks
#SBATCH --output=/home/zhangy15/projects/WGS_de_novo_analysis/script/raw_trio_merge.log/slurm-%A_%a.out
#SBATCH --error=/home/zhangy15/projects/WGS_de_novo_analysis/script/raw_trio_merge.log/slurm-%A_%a.err
#SBATCH -c 1
#SBATCH --mem=16G

# Read 
trio=$(sed -n "$SLURM_ARRAY_TASK_ID"p /home/zhangy15/projects/WGS_de_novo_analysis/script/family_id_file/family_trio_case_control)
IFS=$'\t' read -r -a array <<< $trio

family_id=${array[0]}
patient_id=${array[1]}
parentA=${array[2]}
parentB=${array[3]}

bcftools merge /mnt/isilon/wang_lab/shared/SPARK/WGS/individual_samples/raw_vcf/$patient_id.gvcf.gz /mnt/isilon/wang_lab/shared/SPARK/WGS/individual_samples/raw_vcf/$parentA.gvcf.gz /mnt/isilon/wang_lab/shared/SPARK/WGS/individual_samples/raw_vcf/$parentB.gvcf.gz -g /home/zhangy15/GATK/Homo_sapiens_assembly38.fasta -O v -o /home/zhangy15/projects/WGS_de_novo_analysis/raw_trio_merge/$patient_id.trio.gvcf.gz

tabix /home/zhangy15/projects/WGS_de_novo_analysis/raw_trio_merge/$patient_id.trio.gvcf.gz


