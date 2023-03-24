import get_all_combinations as gac
import compare
import fst_dict

indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
true_scenario = compare.format_true_populations(gac.make_true("CorrectEcotypeAssignments.csv"), mDict)
possible_scenarios = compare.format_populations(indv, mDict)

#remove duplicates
def remove_duplicates(c1, c2):  # removes combination 2 if it matches combination 1
    c1 = population(c1[0], c1[1])
    c2 = population(c2[0], c2[1])
    return
    
 

#p-value

true_delta_fst = compare.delta_fst_true(true_scenario)
poss_delta_fsts = compare.delta_fst_average(possible_scenarios)
print("possible delta fsts: ", poss_delta_fsts)
print("True delta fst: " , true_delta_fst)

p = compare.calculate_p_value(true_delta_fst, poss_delta_fsts)
print("P-value: ", p)


