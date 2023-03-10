# The mainstage where we call our numerous classes and function

# Function that returns every combination of our list, separated into two lists
# inside one list.
import get_all_combinations as gac

import compare

# Current list of populations we are making the comparisons between
indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']


duplicates = gac.get_combinations(indv)
print(duplicates)
print(len(duplicates))

# Removing duplicates
for count, i in enumerate(duplicates):
    pair = Compare(i[0], i[1])
    for j in duplicates[count+1:]:
        c2 = Compare(j[0], j[1])
        d = pair.Is_duplicate(c2)
        print(d)
        if d:
            print(str(d))



#print(compare.same_diff(get_combinations(indv)))



