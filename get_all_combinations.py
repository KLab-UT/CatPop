import itertools

# Define the individuals
individuals = ['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP']

# Generate all possible combinations of 6 individuals
combinations = itertools.combinations(individuals, 6)

# Assign the remaining individuals to the second group
for combination in combinations:
    FA = list(combination)
    SA = list(set(individuals) - set(FA))
    if len(group2) == 6:
        print("SA:", group1)
        print("FA:", group2)
      # Next step (while in for loop): from all pairwise comparisons, determine which pairs are "same" and which are "diff" based on which set they are in (FA or SA). "Same" comparisons will be those that are in the same set with each other. "Diff" comparisons will not be in the same set.
      # One approach: look in FA set for both names. If they both do OR don't appear there, you know its the same! If only one appears, you know its a "diff" comparisonSee you in an hour or so,