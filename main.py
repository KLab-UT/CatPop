import geneID_dict
import calculate_FST_avg as cfa


dd = geneID_dict.make_dict_dict("exons.popgen.csv")
print(dd)
cfa.identify_significant_loci("exons.popgen.csv", "CorrectEcotypeAssignments.csv")
