# GarterSnakeCombinatorics
Using a permutation test and combinatorics to test for differences in population structure between ecotypes of western terrestrial garter snake.

This software package uses combinatorics to create all possible scenarios of two
population assignments, performs a permutation test for each comparison, and
generates a p-value along with the name of the gene.

# Contents
* Flow of data
* Instructions to implement your comparisons
* Other information

# Flow of Data
## The following lists the files used, the functions, and the inputs/outputs.


### compare.py
**Classes**
Populations

Description: Represents a possible comparison between two populations and has
the attributes pair (POP1, POP2), key (for the fst dictionary), and fst (to
store the fst value), the == operator is overrident so that (POP1, POP2) =
(POP2, POP1), as this will account for 'mirror images.'

Attributes: pair, key, fst

Methods: __eq__,get_pair(),get_key(),get_fst(),make_key()

**Functions**

is_float

Description: Returns bool indicating whether parameter is a float.

find_duplicates

Description: Determines if two objects are the same, and returns boolean

get_populations

Description: Takes in array of populations, and returns possible combinations of
the populations.

combine_lists

Description: Combines two lists by appending all elements, in the order in which
they appear in the input lists, and returns the new, combined list.

format_populations

Description: takes in an array of pairs of lists of populations A and a
dictionary of Fst values fst_dict. For each pair of populations in A, it
generates all possible pairwise comparisons of the populations in the two lists
and creates a Populations object for each comparison. It assigns the appropriate
Fst value to each object by calling the make_key function and then appends the
object to either the same or diff list depending on whether it belongs to the
same population or not. It returns a tuple of lists containing all the same and
diff objects for each pair of populations in A.

format_true_populations

Description: The format_true_populations function takes in two lists of
populations (true_lists) and a dictionary of Fst values (fst_dict). It generates
all possible pairwise comparisons between the populations in the two lists,
creates a Populations object for each comparison, assigns the appropriate Fst
value to each object by calling the make_key function, and then appends the
object to either the same or diff list depending on whether it belongs to the
same population or not.


### get_all_combinations.py
**Functions**
get_populations
What it does: Opens and reads formatted file, and returns
Parameters: filename
Input: Formatted file,

