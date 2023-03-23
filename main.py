import get_all_combinations as gac
import compare
import fst_dict


indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
compares = compare.format_populations(indv, mDict)
avgs = compare.same_diff_avg(compares[0], compares[1])
print("Same averages: ", avgs[0])
print("Diff averages: ", avgs[1])

duplicates = gac.get_combinations(indv)
#print(duplicates)
print(len(duplicates))

# Removing duplicates
dup_count = 0
for count, i in enumerate(duplicates):
    pair = compare.Compare(i[0], i[1])
    for j in duplicates[count+1:]:
        c2 = compare.Compare(j[0], j[1])
        d = pair.Is_duplicate(c2)
        if d:
            dup_count += 1
print(dup_count)