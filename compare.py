# The Compare class is used to compare two pairs of values for equality,
# regardless of their order, and returns a string representation of the pair.
# When using the __eq__ method, the c2 is the argument passed into the
# function, and would be the list of populations.

class Compare:
    def __init__(self, a, b):
        self.pair = (a, b)
        self.key = None
        self.fst = None
    def strip_sort(self):
        self.strip()
        
    def Is_duplicate(self, c2):
        if self.pair[0] == c2.pair[0] and self.pair[1] == c2.pair[1]:
            return True
        if self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False

    def Get_pair(self):
        return (str(self.pair[0]), str(self.pair[1]))
    
    
    #TODO generate fst key for given compare and makes sure it is valid for the fst dictionary
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
# return a list of all possible compares in A

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


##Take a list of pairs of lists of populations, for each pair, checks if there are any unique comparisons between the
#pair that are not possible within the idividual lists of populations
#Tracks the number of unique comparisons possible within the separate lists (same) and between the two lists (diff)
#Takes a dictionary with {["Fst_pop1_pop2"]:[fst]} and assigns each compare with its correst key and fst value
#returns a list of unique (diff) comparisons

def same_diff(A, mDict):

    for b in B:
        combined.append(b)

    return combined #the new, combined list

# Take a list of pairs of lists of populations, for each pair, checks if there are any unique comparisons between the pair that are not possible within the idividual lists of populations
# returns the number of unique comparisons possible within the separate lists (same) and between the two lists (diff) 
# idk if this is what we want because it finds no unique comparissons
#
# Takes a list of pairs of values 'A', anc creates a list of all pairwise
# comparisons of the elements in the first two pairs of values, checks which of
# these pairs are same or diff, and prints total number of unique pairs with
# diff values.


def same_diff(A):
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
    return (keys)
            
    


#    return (same, diff)

