import geneID_dict
import calculate_FST_avg as cfa
import random_fst_test as rft

rft.make_fst_file(8, 547)
print('Hello!')
cfa.identify_significant_loci("random_fst_test.csv", "CategoryAssignments_test.csv")
#cfa.identify_significant_loci("exons.popgen.csv", "CorrectEcotypeAssignments.csv")

