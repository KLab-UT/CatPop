# Takes in our extremely long output of FA's and SA's, and puts the first occurrence of FA and SA into
# our first group.


#import get_all_combinations



example = ['A','B','c','D','E','F']
FA = [ 'a', 'b', 'c', 'd', 'e', 'f']
SA = [ 'A', 'B' 'C' 'D', 'E', 'F']

def compare(A,L1,L2):
    i = 1
    same_count = 0
    diff_count =0
    while i < len(A):
        comparison = (A[0], A[1])
        if comparison[0] in L1 and comparison[1] in L1:
            same_count += 1
        if comparison[0] in L2 and comparison[1] in L2:
            same_count += 1
            print(comparison[0], comparison[1])
        else:
            diff_count += 1
        i += 1

    print ("same:", same_count)
    print ("diff:" , diff_count)

compare(example, FA, SA)




class Comparison:
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
            compares.append(Comparison(A[i], A[j]))
            
    return compares

#return a tuple of the number of possible compares (same, different) in two lists 
def checkCompares(A, B):
    A_comps = getCompares(A)
    B_comps = getCompares(B)
    same = 0
    diff = 0
    for i in A_comps:
        if i in B_comps:
            same +=1
        else:
            diff +=1
    
    return(same, diff)

#return a tuple of the number of possible compares (same, different) in three lists 
def checkCompares(A, B, C):
    A_comps = getCompares(A)
    B_comps = getCompares(B)
    C_comps = getCompares(C)
    same = 0
    diff = 0
    found = False
    for i in A_comps:
        for j in B_comps:
            if i==j:
                same +=1
                found = True
        for k in C_comps:
            if i==k:
                same +=1
                found = True
        if not found:
            diff+=1
        
    
    return(same, diff)

a = ['a','b','c','d','e','f']
b = ['x','b','c','d','e','f']
print(checkCompares(example, FA, SA))


'''
def is_value_in_list(list_name,value):
    for i in list_name:
        if value in list_name:
            return True
        return False

def compare_values(L1,value1,value2):
    a = is_value_in_list(L1,value1)
    b = is_value_in_list(L1,value2)
    if a and b == True:
        return "same"
    return "different"

print(compare_values(FA,'a', 'a'))
'''
