setwd("/home/zhangy15/projects/WGS_de_novo_analysis/Revise_denovo_7152024/")

#install.packages('denovolyzeR')
# Load the denovolyzeR library
library(denovolyzeR)

# Read the dataset
autismDeNovos <- read.csv('DNM_summary_expected', sep="\t")

# Calculate ppois for coding variants
ppois_coding <- ppois(q=autismDeNovos$coding_DNM_case-1, # Observed - 1
                      lambda=autismDeNovos$expected_coding, # Expected
                      lower.tail=FALSE)

#Calculate ppois for coding variants
ppois_mis <- ppois(q=autismDeNovos$mis_DNM_case-1, # Observed - 1
                   lambda=autismDeNovos$expected_mis, # Expected
                   lower.tail=FALSE)

# Calculate ppois for coding variants
ppois_lof <- ppois(q=autismDeNovos$lof_DNM_case-1, # Observed - 1
                   lambda=autismDeNovos$expected_lof, # Expected
                   lower.tail=FALSE)

# Calculate ppois for coding variants
ppois_syn <- ppois(q=autismDeNovos$syn_DNM_case-1, # Observed - 1
                   lambda=autismDeNovos$expected_syn, # Expected
                   lower.tail=FALSE)

# Calculate ppois for non-coding variants
ppois_noncoding <- ppois(q=autismDeNovos$noncoding_DNM_cadd_case-1, # Observed - 1
                         lambda=autismDeNovos$expected_noncoding, # Expected
                         lower.tail=FALSE)

# Combine the original data with the new ppois results
results <- data.frame(autismDeNovos, ppois_coding, ppois_mis, ppois_lof, ppois_syn, ppois_noncoding)

write.csv(results, 'DNM_summary_fisher_possion', row.names=FALSE)

