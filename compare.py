'''A Population object represents a possible comparison between two populations and has the attributes pair(POP1, POP2), key (for the fst dictionary), and fst
(to store thr fst value), the == operator is overridden so that (POP1, POP2) = (POP2, POP1). The class includes the getKey function which
generates a valid fst key for a compare and assigns the compare fst (self.fst) to the appropriate value from the given fst dictionary
compare.py also contains the functions; getCompares, which returns a list of all possible compares (one population to another) in the given list of populations
combine_lists, which add two lists of populations together, format_compares which formats compares by creating compare objects and calling getKey, then returns any
unique comparisons found in the combined list that are not in the uncombined lists, and avg_fst which takes a list of compares and returns the average fst '''


class Populations:
    '''
    A class to represent the two populations being compared.

    ...

    Attributes
    ----------
    pair : tuple
        Initializes the populations being paired (pop1,pop2)

    key : int
        The value associated with the population comparisons

    fst : int
        A spot for storing the actual fst value

    Methods
    -------
    __eq__(c2)
        Initates c2 as population object, and checks if first object and
        second are the same.

    get_pair()
        Returns pair of populations

    get_key()
        Returns key

    get_fst()
        Returns fst as float

    make_key()
        Generates valid fst key, and assigns the compare fst (self.fst) to the appropriate value from the dictionary

    '''

    def __init__(self, pop1, pop2):
        '''Initializes population being paired'''
        self.pair = (pop1, pop2)
        self.key = None
        self.fst = None

    def __eq__(self, c2):
        '''Returns bool if objects are mirror images'''
        if self.pair[0] == c2.pair[0] and self.pair[1] == c2.pair[1]:
            return True
        elif self.pair[0] == c2.pair[1] and self.pair[1] == c2.pair[0]:
            return True
        return False

    def get_pair(self):
        '''Returns pair of populations'''
        return (str(self.pair[0]), str(self.pair[1]))

    def get_key(self):
        return self.key

    def get_fst(self):
        return float(self.fst)

    def make_key(self, mDict):
        '''Generates valid Fst key, and assigns appropriate value to the dictionary'''
        key1 = ("Fst_" + str(self.pair[0]) + "_" + str(self.pair[1]))
        key2 = ("Fst_" + str(self.pair[1]) + "_" + str(self.pair[0]))
        if key1 in mDict:
            self.key = key1
            self.fst = mDict[key1]


        elif key2 in mDict:
            self.key = key2
            self.fst = mDict[key2]

        else:
            print(mDict)
            print("Error!, ", key1, "and", key2, "not found ")

def is_float(string):
    '''Returns bool indicating whether parameter is a float'''
    if string.replace(".", "").replace("-","").isnumeric():
        return True
    else:
        return False

def find_duplicates(self, c2):
    '''Determines if first object and second object are same, returns bool'''
    if self == c2:
        return True
    return False


def get_populations(A):
    '''
    Takes in A (array of pops.) and returns possible
    combinations of populations
    '''
    compares = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            c = Populations(A[i], A[j])
            compares.append(c)
    return compares



def combine_lists(A, B):
    '''
    Combines list A and B by appending all elements to combined, in the order in
    which they appear in the input lists and returns the new, combined list..
    '''

    combined = []
    for a in A:
        combined.append(a)
    for b in B:
        combined.append(b)
    return combined


def format_populations(A, fst_dict):
    ''' Takes in dictionary of {Populations:Fst} and assigns with correct key
    and fst values. Returns dictionaries of (same,diff).'''
    total_same = []
    total_diff = []
    for j in range(len(A)): # delete this if you just want to do one pair (66 comparisons) # A[j] is each pair of 12 choose 6
        same = []
        diff = []
        left = get_populations(A[j][0])
        right = get_populations(A[j][1])
        possible_compares = get_populations(combine_lists(A[j][0], A[j][1]))
        for i in possible_compares:
            i.make_key(fst_dict)
            if is_float(i.fst):
                if i in left or i in right:
                    same.append(i)
                else:
                    diff.append(i)
#             else:
#                 print(fst_dict)
#                 print("Error! Fst for ", i.key, " not found")
        total_same.append(same)
        total_diff.append(diff)
    return (total_same, total_diff)
    # Returns (same,diff) where keys are 0-len(A) for each pop. pair in A

def format_true_populations(true_lists, fst_dict):
    '''Takes in two lists of pops and dictionary of Fst values. Generates all
    possible pairwise comparisons between pops in two lists, creates and append
    the object to either same or diff list depending on whether it belongs to
    same population or not.'''
    same = []
    diff = []
    true_1 = get_populations(true_lists[0])
    true_2 = get_populations(true_lists[1])
    possible_compares = get_populations(combine_lists(true_lists[0], true_lists[1]))
    for i in possible_compares:
        i.make_key(fst_dict)
        if is_float(i.fst):
            if i in true_1 or i in true_2:
                same.append(i)
            else: diff.append(i)
    return(same, diff)

