# The mainstage where we call our numerous classes and function

# Function that returns every combination of our list, separated into two lists
# inside one list.
import get_all_combinations as gac

import compare
import calculate_FST_avg as cfa
# Current list of populations we are making the comparisons between
indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']


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


# get average fst
diff_fst_averages = []
same_fst_averages = []
for i in duplicates:
    fst_dictionary = cfa.Make_fst_dictionary("PracticeFstData_OneGene.csv")
    same_fst_averages.append(cfa.Same_fst_avg(i[0], i[1], fst_dictionary)) 
    diff_fst_averages.append(cfa.Diff_fst_avg(i[0], i[1], fst_dictionary)) 

#Rounding float values down to 3 decimal places before printing
for count, f in enumerate(same_fst_averages):
    f = round(f, 3)
    same_fst_averages[count] = f
for count, f in enumerate(same_fst_averages):
    f = round(f, 3)
    diff_fst_averages[count] = f

print("Same: ", same_fst_averages)
print("\n")
print("Different: ", diff_fst_averages) 

#print(compare.same_diff(get_combinations(indv)))



