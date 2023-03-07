class Compare:
    def __init__(self, a, b):
        self.pair = (a, b)
        
    def __eq__(self, c2):
        if self.pair[0] == c2.pair[0] and self.pair[1] == c2.pair[1]:
            return True
        if self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False
    
    def __str__(self):
        return (str(self.pair[0]), str(self.pair[1]))


#return a list of all possible compares in A
def getCompares(A):
    compares = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            c = Compare(A[i], A[j])
            compares.append(c)      
    return compares



def combine_lists(A, B):
    combined = []
    for a in A:
        combined.append(a)
    
    for b in B:
        combined.append(b)

    return combined #the new, combinded list




##Take a list of pairs of lists of populations, for each pair, checks if there are any unique comparisons between the pair that are not possible within the idividual lists of populations
#returns the number of unique comparisons possible within the separate lists (same) and between the two lists (diff) 
#idk if this is what we want because it finds no unique comparissons
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
    for i in comps:
        print(i.pair)
        print(A[0][0])
        print(A[0][1])
        if i in getCompares(A[0][0]) or i in getCompares(A[0][1]): 
            same +=1
        else:
            print("Diff!")
            diff +=1
            unique.append(i)
    print("Total unique: ", len(unique))
    return (same, diff)
            
    



