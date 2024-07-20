import pandas as pd
import pysam
import sys

gt_to_num_map={(0,0):0, (None,None):0,(None,0):0,(0,None):0, (0,1):1, (1,0):1, (None,1):1, (1,None):1, (1,1):2}
patient_id=sys.argv[1]
parentA=sys.argv[2]
parentB=sys.argv[3]
print("Processing: {}  {}  {}".format(patient_id, parentA, parentB))
input_file_path='/home/zhangy15/projects/WGS_de_novo_analysis/de_novo_nomad/%s.de.novo.final.vcf.gz' %patient_id
output_summary_file='/home/zhangy15/projects/WGS_de_novo_analysis/de_novo_summary/case/%s.de_novo_summary.vcf.gz' %patient_id

input_vcf=pysam.VariantFile(input_file_path,'r')
with open(output_summary_file,'w') as summary_file:
    for record in input_vcf:
        rec='\t'.join([patient_id, record.chrom, str(record.pos), str(record.id), record.info.get('Gene.refGene')[0], record.info.get('Func.refGene')[0], record.info.get('ExonicFunc.refGene')[0]])+'\n'
        summary_file.write(rec)



