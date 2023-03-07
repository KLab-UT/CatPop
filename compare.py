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

#Takes three lists, A, B, and C and returns the number of compares in a that are same and different in B and C 
def checkCompares(A, B, C):
    A_comps = getCompares(A)
    B_comps = getCompares(B)
    C_comps = getCompares(C)
    same = 0
    diff = 0
    for i in A_comps:
        if i in B_comps:
            same +=1
        elif i in C_comps:
            same+=1
            
        else:
            diff +=1
    
    return(same, diff)

a = ['x','B','c','d','e']
b = ['a','b','c','d','e']
c = ['A', 'B', 'x', 'D', 'E']


def combine_lists(A, B):
    
    for b in B:
        A.append(b)
    #print("hello")
    #print("Combined: ", A)

    return A #the new, combinded list




#Take a list of pairs of lists of populations, for each pair, checks if there are any unique comparisons between the pair that are not possible within the idividual lists of populations
#returns the number of unique comparisons possible within the separate lists (same) and between the two lists (diff) 
#idk if this is what we want because it finds no unique comparissons
def same_diff(A):
    #print(A)
    unique = []
    same = 0
    diff = 0
    for j in range(len(A)):
        # A[j] is each pair of 12 choose 6
        possible = combine_lists(A[j][0], A[j][1])
        comps = getCompares(possible)
        #print("comps length", len(comps))
        for i in comps:
            if i in getCompares(A[j][0]) or i in getCompares(A[j][1]):
                same +=1
                #print("same!")
            else:
                print("Unique: ", i)
                unique.append(i)
                diff +=1
    print("Total unique: ", len(unique))
    return (same, diff)
            
    
    
    
    






c1 = Compare(a,b)
c2 = Compare(b,a)


