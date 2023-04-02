import geneID_dict
import calculate_FST_avg as cfa

print('Hello!')    
cfa.identify_significant_loci("exons.popgen.csv", "CorrectEcotypeAssignments.csv")