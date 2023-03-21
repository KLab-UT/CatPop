'''A Compare object represents a possible comparison between two populations and has the attributes pair(POP1, POP2), key (for the fst dictionary), and fst 
(to store thr fst value)
, the == operatater is overridden so that (POP1, POP2) = (POP2, POP1). The class includes the getKey function which 
generates a valid fst key for a compare and assigns the compare fst (self.fst) to the appropriate value from the given fst dictionary
compare.py also contains the functions; getCompares, which returns a list of all possible compares (one population to another) in the given list of populations
combine_lists, which add two lists of populations together, format_compares which formats compares by creating compare objects and calling getKey, then returns any 
unique comparisons found in the combined list that are not in the uncombined lists, and avg_fst which takes a list of compares and returns the average fst '''


class Compare:
    def __init__(self, a, b):
        self.pair = (a, b)
        self.key = None
        self.fst = None
    def strip_sort(self):
        self.strip()
        
    def __eq__(self, c2):
        if self.pair[0] == c2.pair[0] and self.pair[1] == c2.pair[1]:
            return True
        elif self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False
    #4 dante
    def Is_duplicate(self, c2):
        if self == c2:
            return True
        return False

    def Get_pair(self):
        return (str(self.pair[0]), str(self.pair[1]))
    
    def getKey(self):
        return self.key
    
    def getFst(self):
        return float(self.fst)
    
    #generates valid fst key for given compare and assigns the compare fst (self.fst) to the appropriate value from the dictionary
    def makeKey(self, mDict):
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
        return self

# return a list of all possible compares (one population to another) in A

def getCompares(A):
    compares = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            c = Compare(A[i], A[j])
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

# Takes a list of pairs of values 'A', anc creates a list of all pairwise
# comparisons of the elements in the first two pairs of values, checks which of
# these pairs are same or diff, and prints total number of unique pairs with
# diff values.
#Tracks the number of unique comparisons possible within the separate lists (same) and between the two lists (diff)
#Takes a dictionary with {["Fst_POP1_POP2"]:[fst]} and assigns each compare with its correst key and fst value by calling the makeKey function
#returns a lists of (same, diff) compares

def format_compares(A, mDict):
    total_same = {}
    total_diff = {}
    for j in range(len(A)): # get rid of this if you just want to do one pair (66 comparisons) # A[j] is each pair of 12 choose 6
        same = []
        diff = []
        left = getCompares(A[j][0])
        right = getCompares(A[j][1])
        possible_compares = getCompares(combine_lists(A[j][0], A[j][1]))
        for i in possible_compares:
            i.makeKey(mDict)
            if i in left or i in right:
                same.append(i)
            else:
                diff.append(i)
        total_same[j] = same
        total_diff[j] = diff
    return (total_same, total_diff)
            
            
def avg_fst(compares):
    total = 0.0
    for compare in compares:
        fst = compare.getFst()
        total += fst
    avg = total/len(compares)
    return avg






#TODO
def get_averages(same, diff):

    pass