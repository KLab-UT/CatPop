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
        delta_avg = abs(same_avgs[i] - diff_avgs[i])
        delta_fst_avgs.append(round(delta_avg,3))
    return delta_fst_avgs

def delta_fst_true(true_scenario):
    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])
    delta_fst = round(abs(same_avg - diff_avg), 3)
    return delta_fst

def calculate_p_value(true_delta, poss_deltas):
    qual = 0.0
    for i in poss_deltas:
        if i >= true_delta:
            qual += 1
    p = qual/len(poss_deltas)
    return p


def identify_significant_loci(gene_file, ecotype_file):
    log = open('log.txt', 'w')
    results = open('results.txt', 'w')
    
    dictdict = geneID_dict.make_dict_dict(gene_file)
    gene_list = dictdict.keys()
    genes = []
    
    for key in gene_list:
        genes.append(key)
    
    true_lists = gac.make_true(ecotype_file)
    indv = compare.combine_lists(true_lists[0], true_lists[1])
    combinations = gac.get_combinations(indv)
    
    for gene in genes:
        true_scenario = compare.format_true_populations(true_lists, dictdict[gene])
        true_delta_fst = delta_fst_true(true_scenario)
        possible_scenarios = compare.format_populations(combinations, dictdict[gene])
        poss_delta_fsts = delta_fst_average(possible_scenarios)
        p_value = calculate_p_value(true_delta_fst, poss_delta_fsts)
        this_gene = track_gene(gene, true_delta_fst, p_value, poss_delta_fsts)
        
        for value in this_gene:
            log.write('{0}\n'.format(value))
        if p_value <= 0.05:
            this_gene = this_gene[:3]
            for value in this_gene:
                results.write('{0}\n'.format(value))
    log.close()
    results.close()

def track_gene(gene, true_delta_fst, p_value, poss_delta_fsts):
    this_gene = []
    this_gene.append(gene)
    this_gene.append("True delta fst: " + str(true_delta_fst))
    this_gene.append("p-value: " + str(p_value))
    this_gene.append("Possible delta fsts: " + str(poss_delta_fsts))
    return this_gene

        
        