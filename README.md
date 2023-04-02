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


### get_all_combinations.py
**Functions**
get_populations
What it does: Opens and reads formatted file, and returns
Parameters: filename
Input: Formatted file,

