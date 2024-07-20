import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
dir_path = '/home/zhangy15/projects/WGS_de_novo_analysis/final_summary/'
os.chdir(dir_path)

#case/control
case_gt = pd.read_csv('DNM_summary_case_score_rmlowmap_rm100bp_rmMUC', sep="\t")
ctrl_gt = pd.read_csv('DNM_summary_ctrl_score_rmlowmap_rm100bp_rmMUC', sep="\t")

#Gscore
Gscore=pd.read_csv('/home/zhangy15/projects/scratch/Supplementary_Data_2.bed.gz', sep='\t',header=None)
Gscore.columns=['chr','start','end','Gscore']

# Let's assume df1 and df2 are already loaded pandas DataFrames corresponding to your data1 and data2 respectively.

# First, ensure that the 'chr' columns in both dataframes have the same format.
# This might not be necessary if the formatting is already consistent.
# df1['chr'] = df1['chr'].astype(str)
# Gscore['chr'] = Gscore['chr'].astype(str)

# Creating an interval index from Gscore 'start' and 'end' for efficient range checking
interval_index = pd.IntervalIndex.from_arrays(Gscore['start'], Gscore['end'], closed='both')

# This function is used to find a matching 'Gscore' based on 'pos' and 'chr'
def find_matching_gscore(row):
    # Find the matching interval and chromosome
    mask = interval_index.contains(row['pos']) & (Gscore['chr'] == row['chr'])
    matched_gscores = Gscore.loc[mask, 'Gscore']
    
    # If there's a match, return the 'Gscore' value, otherwise return NaN
    if not matched_gscores.empty:
        return matched_gscores.iloc[0]
    else:
        return pd.NA  # or use np.nan if pd.NA is not suitable

# Apply the function to each row in df1 to find and append the 'Gscore'
case_gt['Gscore'] = case_gt.apply(find_matching_gscore, axis=1)
ctrl_gt['Gscore'] = ctrl_gt.apply(find_matching_gscore, axis=1)

# Display the updated df1 with the 'Gscore' values appended
case_gt.to_csv('/home/zhangy15/projects/WGS_de_novo_analysis/final_summary/case_final', sep='\t')
ctrl_gt.to_csv('/home/zhangy15/projects/WGS_de_novo_analysis/final_summary/ctrl_final', sep='\t')