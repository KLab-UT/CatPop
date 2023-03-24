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


def make_dict(filename):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]
        values = f.readline().strip().split(",")
        mDict = dict(zip(keys, values))
        return mDict

# takes a file where each line is population,ecotype and returns a dictionary {ecotype, [populations in that ecotype]}
def make_true(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    pairs = [line.strip().split(',') for line in lines]
    
    ecotype_dict = {pair[0]: pair[1] for pair in pairs}
    ecotype_dict.pop('ï»¿Population')
    
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

print(make_true("CorrectEcoTypeAssignments.csv"))

