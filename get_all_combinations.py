import itertools
import compare

def get_combinations(individuals, length):
    '''Takes list of individuals as input, generates all possible combinations
    of 6 individuals from given list. Then creates pairs of those
    combinations and removes duplicates'''
    # Generate all possible combinations of length individuals
    combinations = itertools.combinations(individuals, length)

    fa_sa_pairs = []
    # Assign the remaining individuals to the second group
    for combination in combinations:
        FA = list(combination)
        SA = list(set(individuals) - set(FA))
        FA.sort()
        SA.sort()
        if len(FA) == length:
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
        for comparison in fa_sa_pairs[count+1:]:
            c = compare.Populations(comparison[0], comparison[1])
            if ps == c:
                fa_sa_pairs.remove(comparison)

    return fa_sa_pairs

def make_true(filename):
    ''' Takes filename as input, reads file, and creates a list of lists, where
    each inner list contains the names of individuals belonging to same
    ecotype, and returns the final list of ecotypes'''
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]  #remove top line of text file "Ecotype:Populations"
    pairs = [line.strip().split(',') for line in lines]

    ecotype_dict = {pair[0]: pair[1] for pair in pairs}

    indv = ecotype_dict.keys()
    indv_list = []
    for key in indv:
        indv_list.append(key)

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
    f.close()
    return (true_lists)

