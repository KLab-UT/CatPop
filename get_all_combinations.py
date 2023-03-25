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
    # Remove duplicates in fa_sa_pairs
    for count, pop_set in enumerate(fa_sa_pairs):
        ps = compare.Populations(pop_set[0], pop_set[1])
        for comparison in fa_sa_pairs[count:]:
            c = compare.Populations(comparison[0], comparison[1])
            if ps == c:
                fa_sa_pairs.remove(comparison)
                break    #I'm not sure why break fixes the remove duplicates part
    
    return fa_sa_pairs
print ("X: ", len(get_combinations(indv)))
# # make combinations_list and remove duplicates
# combinations_list = get_combinations(indv)
# print(len(combinations_list))
# def remove_duplicates(combinations_list): #compare c1 to c2 and remove c2 if they're identical
#     for count, pop_set in enumerate(combinations_list):
#         ps = compare.Populations(pop_set[0], pop_set[1])
#         for comparison in combinations_list[count:]:
#             c = compare.Populations(comparison[0], comparison[1])
#             if ps == c:
#                 combinations_list.remove(comparison)
#                 break
#     return combinations_list
# print(len(remove_duplicates(combinations_list)))

def make_dict(filename):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]
        values = f.readline().strip().split(",")
        mDict = dict(zip(keys, values))
        return mDict

# takes a file where each line is population,ecotype and returns a nested lists of seperate ecotypes:
def make_true(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    pairs = [line.strip().split(',') for line in lines]
    
    ecotype_dict = {pair[0]: pair[1] for pair in pairs}
    ecotype_dict.pop('Population')
    
    ecotypes = []
    #get different ecotypes
    for key in ecotype_dict:
        if ecotype_dict[key] not in ecotypes:
            ecotypes.append(ecotype_dict[key])
            
    #make true lists
    true_lists = []
    for ecotype in ecotypes:
        this_ecotype = []
        for key in ecotype_dict:
            if ecotype_dict[key] == ecotype:
                this_ecotype.append(key)
        true_lists.append(this_ecotype)

    return (true_lists)


