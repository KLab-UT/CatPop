import get_all_combinations as gac
import compare
import fst_dict


indv = gac.get_combinations(['MAH','MER','PVM','SUM','STO','CHR','RON','ROC','ELF','NAM','MAR','PAP'])
mDict = fst_dict.makeDict("PracticeFstData_OneGene.csv")
possible_scenarios = compare.format_populations(indv, mDict)

possible_avgs = compare.same_diff_avg(possible_scenarios[0], possible_scenarios[1])
pos_same_avgs = possible_avgs[0]
pos_diff_avgs = possible_avgs[1]

true = gac.make_true("CorrectEcoTypeAssignments.csv")
true_scenario = compare.format_true_populations(true, mDict)
true_same_avg = compare.avg_fst(true_scenario[0])
true_diff_avg = compare.avg_fst(true_scenario[1])
 

#p-value

true_delta_fst = abs(true_same_avg - true_diff_avg)
pos_delta_fst = compare.delta_fst_average(pos_same_avgs, pos_diff_avgs)
print("possible Delta fsts: ", pos_delta_fst)
print("True delata fst: " , true_delta_fst)
