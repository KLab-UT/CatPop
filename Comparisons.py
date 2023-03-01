# Takes in our extremely long output of FA's and SA's, and puts the first occurrence of FA and SA into
# our first group.


#import get_all_combinations



example = ['A','B','C','D','E','F']
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
