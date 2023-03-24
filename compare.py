'''A Compare object represents a possible comparison between two populations and has the attributes pair(POP1, POP2), key (for the fst dictionary), and fst 
(to store thr fst value)
, the == operatater is overridden so that (POP1, POP2) = (POP2, POP1). The class includes the getKey function which 
generates a valid fst key for a compare and assigns the compare fst (self.fst) to the appropriate value from the given fst dictionary
compare.py also contains the functions; getCompares, which returns a list of all possible compares (one population to another) in the given list of populations
combine_lists, which add two lists of populations together, format_compares which formats compares by creating compare objects and calling getKey, then returns any 
unique comparisons found in the combined list that are not in the uncombined lists, and avg_fst which takes a list of compares and returns the average fst '''


class Populations:
    def __init__(self, a, b):
        self.pair = (a, b)
        self.key = None
        self.fst = None
        
    def __eq__(self, c2):
        if self.pair[0] == c2.pair[0] and self.pair[1] == c2.pair[1]:
            return True
        elif self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False

    def get_pair(self):
        return (str(self.pair[0]), str(self.pair[1]))
    
    def get_key(self):
        return self.key
    
    def get_fst(self):
        return float(self.fst)
    
    #generates valid fst key for given compare and assigns the compare fst (self.fst) to the appropriate value from the dictionary
    def make_key(self, mDict):
        key1 = ("Fst_" + str(self.pair[0]) + "_" + str(self.pair[1]))
        key2 = ("Fst_" + str(self.pair[1]) + "_" + str(self.pair[0]))
        if key1 in mDict:
            self.key = key1
            self.fst = mDict[key1]
        elif key2 in mDict:
            self.key = key2
            self.fst = mDict[key2]
        else:
            print("Error!, ", key1, "and", key2, "not found ")

# return a list of all possible compares (one population to another) in A

#TODo remove duplicates 
def find_duplicates(self, c2):
    if self == c2:
        return True
    return False


#A is and array of populations
#returns possible combinations of populTIONS 
def get_populations(A):
    compares = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            c = Populations(A[i], A[j])
            compares.append(c)
    return compares


# Combines list A and B by appending all elements to combined, in the order in
# which they appear in the input lists.

def combine_lists(A, B):
    combined = []
    for a in A:
        combined.append(a)
    for b in B:
        combined.append(b)
    return combined #the new, combinded list

# Takes a list of pairs of lists of populations and creates a list of all pairwise
# comparisons of the elements in each two pairs of populations, creates populations objects for each population to population comparison
#Takes a dictionary with {["Fst_POP1_POP2"]:[fst]} and assigns each compare with its correct key and fst value by calling the makeKey function
#returns dictionaries of (same, diff) compares where the keys are 0--len(A) for each pair of populations in A

def format_populations(A, fst_dict):
    total_same = []
    total_diff = []
    for j in range(len(A)): # get rid of this if you just want to do one pair (66 comparisons) # A[j] is each pair of 12 choose 6
        same = []
        diff = []
        left = get_populations(A[j][0])
        right = get_populations(A[j][1])
        possible_compares = get_populations(combine_lists(A[j][0], A[j][1]))
        for i in possible_compares:
            i.make_key(fst_dict)
            if i in left or i in right:
                same.append(i)
            else:
                diff.append(i)
        total_same.append(same)
        total_diff.append(diff)
    return (total_same, total_diff)

def format_true_populations(true_lists, fst_dict):
    same = []
    diff = []
    true_1 = get_populations(true_lists[0])
    true_2 = get_populations(true_lists[1])
    possible_compares = get_populations(combine_lists(true_lists[0], true_lists[1]))
    for i in possible_compares:
        i.make_key(fst_dict)
        if i in true_1 or i in true_2:
            same.append(i)
        else: diff.append(i)
    return(same, diff)
    
   
            
            
def avg_fst(compares):
    total = 0.0
    
    for compare in compares:
        fst = compare.get_fst()
        total += fst
    avg = total/len(compares)
    return round(avg, 3)






#takes a list of lists of  populations objects, returns a list of fst averages fst for each list of populations objects

def possible_avgs(poss_populations):
    avgs = []
    for i in poss_populations:  
        avg = avg_fst(i)
        avgs.append(avg)   
    return(avgs)



#takes a list of  and returns a list of the differences between corresponding elements
def delta_fst_average(poss_populations):
    same_avgs = possible_avgs(poss_populations[0])
    diff_avgs = possible_avgs(poss_populations[1])
    delta_fst_avgs = []
    for i in range(len(same_avgs)):
        delta_avg = abs(same_avgs[i] - diff_avgs[i])
        delta_fst_avgs.append(round(delta_avg,3))
    return delta_fst_avgs

    
def delta_fst_true(true_scenario):
    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])
    delta_fst = round(abs(same_avg - diff_avg), 3)
    return delta_fst
    

def calculate_p_value(true_delta, poss_deltas):
    qual = 0.0
    for i in poss_deltas:
        if i >= true_delta:
            qual += 1
    p = qual/len(poss_deltas)
    return p
        
    