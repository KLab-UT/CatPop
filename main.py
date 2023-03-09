# The mainstage where we call our numerous classes and function

# Function that returns every combination of our list, separated into two lists
# inside one list. Example of a single list: [[A,B,C],[D,E,F]], and in reality,
# there are hundreds of variations of above, such as [[A,B,E,],[D,C,F]] and so
# on.
import get_all_combinations

# Function that removes mirror images/duplicates. This would be like removing
# [[D,E,F], [A,B,C]] from the get_all_combinations, as [[A,B,C],[D,E,F]] and
# [[D,E,F], [A,B,C]] are mirror 'images'
import compare

# Current list of populations we are making the comparisons between
indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']

# When called, returns every possible combinations
print(get_combinations(indv))


#print(compare.same_diff(get_combinations(indv)))



