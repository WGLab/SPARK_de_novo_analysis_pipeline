import pandas as pd
import pysam
import sys

def process_info(x):
    if x==None:
        return 0
    else:
        return x
def process_ad(ad):
    if ad==(None,None):
        return (0,0)
    else:
        return ad

gt_to_num_map={(0,0):0, (None,None):0,(None,0):0,(0,None):0, (0,1):1, (1,0):1, (None,1):1, (1,None):1, (1,1):2}
patient_id=sys.argv[1]
parentA=sys.argv[2]
parentB=sys.argv[3]
print("Processing: {}  {}  {}".format(patient_id, parentA, parentB))
input_file_path='/home/zhangy15/projects/WGS_de_novo_analysis/de_novo_mutation/%s.de_novo.vcf.gz' %patient_id
output_file_path='/home/zhangy15/projects/WGS_de_novo_analysis/de_novo_filter/%s.de_novo_filter.vcf.gz' %patient_id

input_vcf=pysam.VariantFile(input_file_path,'r')
with pysam.VariantFile(output_file_path,'w', header=input_vcf.header) as output_vcf:
    for record in input_vcf:
        if process_ad(record.samples[patient_id]['AD'][1])>=6 and process_info(record.samples[parentA]['GQ'])>=20 and process_info(record.samples[parentB]['GQ'])>=20 and process_info(record.samples[patient_id]['GQ'])>=25:
            output_vcf.write(record)
