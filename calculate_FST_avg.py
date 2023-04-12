import compare
import get_all_combinations as gac
import geneID_dict
def avg_fst(compares):
    total = 0.0
    if len(compares) > 0:
        for populations in compares:
            fst = populations.get_fst()
            total += fst
        avg = total/len(compares)
        return round(avg, 3)
    return total

def possible_avgs(poss_populations):
    '''
    Takes a list of lists of  populations objects, returns a list of fst
    averages fst for each list of populations objects
    '''
    avgs = []
    for i in poss_populations:
        avg = avg_fst(i)
        avgs.append(avg)
    return(avgs)

def delta_fst_average(poss_populations):
    '''
    Takes a list of  and returns a list of the differences between
    corresponding elements
    '''

    same_avgs = possible_avgs(poss_populations[0])
    diff_avgs = possible_avgs(poss_populations[1])
    delta_fst_avgs = []
    for i in range(len(same_avgs)):
        delta_avg = round(abs(same_avgs[i] - diff_avgs[i]),3)
        delta_fst_avgs.append(delta_avg)
    return delta_fst_avgs

def true_fst_same_diff(true_scenario):

    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])

    return (same_avg, diff_avg)

def delta_fst_true(true_scenario):
    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])
    delta_fst = round(abs(same_avg - diff_avg),3)
    return delta_fst



def calculate_p_value(true_delta, poss_deltas):
    qualifying = []
    qual = 0 #numerator always at least 1 because of true delta
    length = len(poss_deltas)
    for i in poss_deltas:
        if i >= true_delta:
            qualifying.append(i) 
            qual += 1
    p = qual/length
    return (p, qual, length)


def identify_significant_loci(gene_file, ecotype_file):
    log = open('log.txt', 'w')
    results = open('results.txt', 'w')
    
    sig_output = open('sig_output.csv' , 'w')
    all_output = open('all_output.csv' , 'w')
    sig_output.write('GeneID,P-value,Significant,TrueDeltaSame,TrueDeltaDiff,\n')
    all_output.write('GeneID,P-value,Significant,TrueDeltaSame,TrueDeltaDiff,\n')
    
    dictdict = geneID_dict.make_dict_dict(gene_file)
    
    true_lists = gac.make_true(ecotype_file)
    indv = compare.combine_lists(true_lists[0], true_lists[1])
    print("indv: ", indv)
    combinations = gac.get_combinations(indv, len(indv)//2)
    print('combinations: ', combinations, "length: ", len(combinations))
    
    print('Thinking...')
    for gene in dictdict:
        true_scenario = compare.format_true_populations(true_lists, dictdict[gene])
        true_delta_fst = delta_fst_true(true_scenario)
        possible_scenarios = compare.format_populations(combinations, dictdict[gene])
        poss_delta_fsts = delta_fst_average(possible_scenarios)
        same_diff_true = true_fst_same_diff(true_scenario)
        p = calculate_p_value(true_delta_fst, poss_delta_fsts)
        this_gene = track_gene(gene, true_delta_fst, p, poss_delta_fsts)
        p_value = p[0]
        sig = 0
        for value in this_gene:
            log.write('{0}\n'.format(value))
        line = gene + ',' + str(p_value) + ',' + str(sig) +','+ str(same_diff_true[0]) +','+ str(same_diff_true[1]) + '\n'
        if p_value <= 0.05:
            sig = 1
#             this_gene.pop(3)
#             this_gene.pop(4)
#             this_gene.pop()
        
            for value in this_gene:
                results.write('{0}\n'.format(value))
            sig_output.write(line)
            all_output.write(line)
        else:
            all_output.write(line)
    log.close()
    results.close()
    sig_output.close()
    all_output.close()
    print("Finished! See sig_output.csv, all_output.csv, results.txt, and log.txt")

def track_gene(gene, true_delta_fst, p, poss_delta_fsts):
    this_gene = []
    this_gene.append(gene)
    this_gene.append("True delta fst: " + str(true_delta_fst))
    this_gene.append("p-value: " + str(p[0]))
    this_gene.append("Possible delta fsts: " + str(poss_delta_fsts))
    this_gene.append("Qualifiers: " + str(p[1]))
    this_gene.append("Total: " + str(p[2]))
    this_gene.append("\n")
    #print("this_gene: ", this_gene)
    return this_gene

        
        
