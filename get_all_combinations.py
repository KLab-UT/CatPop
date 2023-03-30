import itertools
import compare

def get_populations(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]  #remove top line of text file "Ecotype:Populations"
        pairs = [line.strip().split(':') for line in lines]

        populations = [pair[1].strip().split(',') for pair in pairs] #get populations seperate from ecotype
        p = populations[0]+populations[1] #combine populations insto one list
        return p

#indv = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']
#indv = get_populations("Alternative_layout_CEA.csv")
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
        for comparison in fa_sa_pairs[count+1:]:
            c = compare.Populations(comparison[0], comparison[1])
            if ps == c:
                fa_sa_pairs.remove(comparison)

    return fa_sa_pairs

def make_dict(filename):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]
        values = f.readline().strip().split(",")
        mDict = dict(zip(keys, values))
        return mDict




def make_dict_dict(filename):
    f=open(filename, "r")
    first=f.readline()
    popComb=first.strip().split(",")[1:]
    dd = {}
    for line in f:
        geneID=line.strip().split(",")[:1]
        fsts=line.strip().split(",")[1:]
        dict_popComb={popComb[0]:fsts[0]}
        for i in range(1,len(popComb)):
            dict_popComb[popComb[i]]=fsts[i]
        dd[geneID[0]] = dict_popComb
        
    return dd

# takes a file where each line is population,ecotype and returns a nested lists of seperate ecotypes:
def make_true(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]  #remove top line of text file "Ecotype:Populations"
    pairs = [line.strip().split(',') for line in lines]

    ecotype_dict = {pair[0]: pair[1] for pair in pairs}
    print(ecotype_dict)
    indv = ecotype_dict.keys()
    indv_list = []
    for key in indv:
        indv_list.append(key)
    #ecotype_dict.pop('ï»¿Population')

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

