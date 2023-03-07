# Takes in our extremely long output of FA's and SA's, and puts the first occurrence of FA and SA into
# our first group.
# This function doesn't necessarily complete what we are trying to accomplish


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


