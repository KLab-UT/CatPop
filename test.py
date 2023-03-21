'''Reagan's test file'''
import get_all_combinations as gac
import compare
import fst_dict


indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
compares = compare.format_compares(indv, mDict)
same_avgs =[]
diff_avgs = []

for i in range(len(compares[0])): #same
    avg = compare.avg_fst(compares[0][i])
    same_avgs.append(avg)
for i in range(len(compares[1])): #diff
    avg = compare.avg_fst(compares[1][i])
    diff_avgs.append(avg)
    
print("Same averages: ", same_avgs)
print("Diff averages: ", diff_avgs)

# for i in same:
#     print(i.key)
#     print(i.fst)
# print("Same average: ", avg_same)
#     
# for i in diff:
#     print(i.key)
#     print(i.fst)
# print("Diff average: ", avg_diff)


    