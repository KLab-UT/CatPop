'''A Compare object represents a possible comparison between two populations and has the attributes pair(POP1, POP2), key (for the fst dictionary), and fst 
(to store thr fst value)
, the == operatater is overridden so that (POP1, POP2) = (POP2, POP1). The class includes the getKey function which 
generates a valid fst key for a compare and assigns the compare fst (self.fst) to the appropriate value from the given fst dictionary
compare.py also contains the functions; getCompares, which return a list of all possible compares (one population to another) in the given list of populations
combine_lists, which add two lists of populations together, and same_diff which formates compares by creating compare objects and calling getKey, then returns any 
unique comparisons found in the combined list that are not in the uncombined lists'''


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
        if self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False

    def Get_pair(self):
        return (str(self.pair[0]), str(self.pair[1]))
    
    
    #generates valid fst key for given compare and assigns the compare fst (self.fst) to the appropriate value from the dictionary
    def getKey(self, mDict):
        key1 = ("Fst_" + str(self.pair[0]) + "_" + str(self.pair[1]))
        key2 = ("Fst_" + str(self.pair[1]) + "_" + str(self.pair[0]))
        print(key1)
        print(key2)
        if key1 in mDict:
            self.key = key1
            self.fst = mDict[key1]
        elif key2 in mDict:
            self.key = key2
            self.fst = mDict[key2]
        else:
            print("Error! key not found ")
        return self

# Creates a list of Class Compare objects that represent all possible pairwise
# comparisons of elements in the input list. This list can be used to compare
# elements in the input list using __eq__ method of the Compare Class
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
#Takes a dictionary with {["Fst_POP1_POP2"]:[fst]} and assigns each compare with its correst key and fst value by calling th makeKey function
#returns a list of unique (diff) compares 

def same_diff(A, mDict):
    #print(A)
    unique = []
    same = 0
    diff = 0
    #for j in range(len(A)): # get rid of this if you just want to do one pair (66 comparisons)
        # A[j] is each pair of 12 choose 6
    possible = combine_lists(A[0][0], A[0][1])
    comps = getCompares(possible)
    #print("comps length", len(comps))
    keys = []
    for i in comps:
        keys.append(i.getKey(mDict))
        if i in getCompares(A[0][0]) or i in getCompares(A[0][1]): 
            print(i.pair)
            print(A[0][0])
            print(A[0][1])
        if i in getCompares(A[0][0]) or i in getCompares(A[0][1]):
            same +=1
        else:
            diff +=1
            unique.append(i)
    print("Total unique: ", len(unique))
    return (unique)
            
    


