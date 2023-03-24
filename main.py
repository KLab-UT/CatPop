import get_all_combinations as gac
import compare
import fst_dict


indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
possible_scenarios = compare.format_populations(indv, mDict)
true_scenario = compare.format_true_populations(gac.make_true("CorrectEcoTypeAssignments.csv"), mDict)
 

#p-value

true_delta_fst = compare.delta_fst_true(true_scenario)
pos_delta_fst = compare.delta_fst_average(possible_scenarios)
print("possible delta fsts: ", pos_delta_fst)
print("True delta fst: " , true_delta_fst)
