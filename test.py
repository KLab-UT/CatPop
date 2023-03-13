'''Reagan's test file'''
import get_all_combinations as gac
import compare
import fst_dict


indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
compares = compare.format_compares(gac.get_combinations(indv), mDict)
same = compares[0]
diff = compares[1]
avg_same = compare.avg_fst(same)
avg_diff = compare.avg_fst(diff)

for i in same:
    print(i.key)
    print(i.fst)
print("Same average: ", avg_same)
    
for i in diff:
    print(i.key)
    print(i.fst)
print("Diff average: ", avg_diff)


    