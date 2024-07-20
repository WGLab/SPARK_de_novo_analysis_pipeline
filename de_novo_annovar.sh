#!/bin/bash

#SBATCH --time=12:00:00
#SBATCH --array=1-5697    # create n tasks
#SBATCH --output=/home/zhangy15/projects/WGS_de_novo_analysis/script/de_novo_filter_DP.log/anno_slurm-%A_%a.out
#SBATCH --error=/home/zhangy15/projects/WGS_de_novo_analysis/script/de_novo_filter_DP.log/anno_slurm-%A_%a.err
#SBATCH -c 1
#SBATCH --mem=16G

# Read 
trio=$(sed -n "$SLURM_ARRAY_TASK_ID"p /home/zhangy15/projects/WGS_de_novo_analysis/script/family_id_file/family_trio_case_control)
IFS=$'\t' read -r -a array <<< $trio

family_id=${array[0]}
patient_id=${array[1]}
parentA=${array[2]}
parentB=${array[3]}

/home/zhangy15/projects/genomics_exercise/annovar/table_annovar.pl /home/zhangy15/projects/WGS_de_novo_analysis/de_novo_filter_DP/$patient_id.de_novo_filter_DP.vcf.gz /home/zhangy15/projects/genomics_exercise/annovar/humandb/ -buildver hg38 -out /home/zhangy15/projects/WGS_de_novo_analysis/de_novo_annovar/myanno.$patient_id.de_novo_filter -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp42a,gnomad_exome,gnomad312_genome,clinvar_20221231 -operation gx,r,f,f,f,f,f,f -nastring . -vcfinput -polish




