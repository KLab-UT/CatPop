import itertools
import compare
indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']
def get_combinations(individuals):
    # Generate all possible combinations of 6 individuals
    combinations = itertools.combinations(individuals, 6)

    fa_sa_pairs = []
    # Assign the remaining individuals to the second group
    for combination in combinations:
        FA = list(combination)
        SA = list(set(individuals) - set(FA))
        FA.sort()
        SA.sort()
        if len(FA) == 6:
            # Create a new list to hold the FA and SA pairs for this combination
            current_pairs = []
            # Append the FA and SA lists to the current pairs list
            current_pairs.append(FA)
            current_pairs.append(SA)
            # Append the current pairs list to the list of pairs for all combinations
            fa_sa_pairs.append(current_pairs)
    return fa_sa_pairs


def makeDict(filename):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]
        values = f.readline().strip().split(",")
        mDict = dict(zip(keys, values))
        return dict(zip(keys, values))



# mDict = makeDict("PracticeFstData_OneGene.csv")
# mKeys = compare.format_compares(get_combinations(indv), mDict)
# found = 0
# total = 0
# print(len(mKeys))
# print(len(mDict))
# print(mKeys)
# for mkey in mKeys:
#     if mkey.key in mDict:
#         found +=1
#     else:
#         print(mkey)
#
# print(found)



# for i, pair in enumerate(fa_sa_pairs):
#     print(f"Pair {i}: {pair}")

