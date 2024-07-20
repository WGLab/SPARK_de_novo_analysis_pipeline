import pandas as pd
import pysam
import sys
gt_to_num_map={(0,0):0, (None,None):0,(None,0):0,(0,None):0, (0,1):1, (1,0):1, (None,1):1, (1,None):1, (1,1):2}
patient_id=sys.argv[1]
parentA=sys.argv[2]
parentB=sys.argv[3]
print("Processing: {}  {}  {}".format(patient_id, parentA, parentB))
input_file_path='/home/zhangy15/projects/WGS_de_novo_analysis/raw_trio_norm/%s.trio.norm.gvcf.vcf.gz' %patient_id
output_file_path='/home/zhangy15/projects/WGS_de_novo_analysis/de_novo_mutation/%s.de_novo.vcf.gz' %patient_id

input_vcf=pysam.VariantFile(input_file_path,'r')
with pysam.VariantFile(output_file_path,'w', header=input_vcf.header) as output_vcf:
    for record in input_vcf:
        if gt_to_num_map[record.samples[patient_id]['GT']]>=1 and gt_to_num_map[record.samples[parentA]['GT']]==0 and gt_to_num_map[record.samples[parentB]['GT']]==0:
            output_vcf.write(record)
