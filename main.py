import get_all_combinations as gac
import compare
import fst_dict


indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
compares = compare.format_compares(indv, mDict)
avgs = compare.same_diff_avg(compares[0], compares[1])
print("Same averages: ", avgs[0])
print("Diff averages: ", avgs[1])
