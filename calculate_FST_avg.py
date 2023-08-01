import compare
import get_all_combinations as gac
import geneID_dict
def avg_fst(compares):
    '''
    This function calculates the average value of the "fst" property for a
    collection of populations and returns the result rounded to three decimal
    places. If the collection is empty, it returns 0.0
    '''
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
    Takes a list of [same, diff] populations objects and returns a list of the avegarge delta fst
    '''
    same_avgs = possible_avgs(poss_populations[0])
    diff_avgs = possible_avgs(poss_populations[1])
    delta_fst_avgs = []
    for i in range(len(same_avgs)):
        delta_avg = round(abs(same_avgs[i] - diff_avgs[i]),3)
        delta_fst_avgs.append(delta_avg)
    return delta_fst_avgs

def true_fst_same_diff(true_scenario):
    '''Returns the averages of the same and diff scenarios'''
    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])

    return (same_avg, diff_avg)

def delta_fst_true(true_scenario):
    ''' Returns the delta_fst's that are larger than the actual delta_fst'''
    same_avg = avg_fst(true_scenario[0])
    diff_avg = avg_fst(true_scenario[1])
    delta_fst = round(abs(same_avg - diff_avg),3)
    return delta_fst



def calculate_p_value(true_delta, poss_deltas):
    '''
    This function calculates the p-value by determining the ratio of qualifying
    elements (elements greater than or equal to true_delta) to the total number
    of elements in the poss_deltas collection. It also returns the number of
    qualifying elements and the length of poss_deltas as additional
    information.
    '''
    qualifying = []
    qual = 0 #numerator always at least 1 because of true delta
    length = len(poss_deltas)
    for i in poss_deltas:
        if i >= true_delta:
            qualifying.append(i)
            qual += 1
        if i == "NA":
            print("problem")
    p = qual/length
    return (p, qual, length)


def identify_significant_loci(gene_file, ecotype_file):
    '''
    This function performs various data processing and analysis tasks to
    identify significant loci based on genetic and ecotype data. It writes logs
    and results to files and outputs a completion message when finished.
    '''
    log = open('log.txt', 'w')
    results = open('results.txt', 'w')

    sig_output = open('sig_output.csv' , 'w')
    all_output = open('all_output.csv' , 'w')
    sig_output.write('GeneID,P-value,Significant,TrueDeltaSame,TrueDeltaDiff,\n')
    all_output.write('GeneID,P-value,Significant,TrueDeltaSame,TrueDeltaDiff,\n')

    dictdict = geneID_dict.make_dict_dict(gene_file)
    log.write("******************************\ndictdict\n*********************************\n")
    for item in dictdict:
        log.write("\n\nnew item:\n")
        log.write(str(item) + "\n")
        log.write(str(dictdict[item]) + "\n")

    true_lists = gac.make_true(ecotype_file)
    log.write("\n\n\n******************************\ntrue_lists\n*********************************\n")
    log.write(str(true_lists)+ "\n")

    indv = compare.combine_lists(true_lists[0], true_lists[1])
    log.write("\n\n\n******************************\nindv\n*********************************\n")
    log.write("indv: "+ str(indv) + "\n")
    combinations = gac.get_combinations(indv, len(indv)//2)
    log.write("\n\n\n******************************\ncombinations\n*********************************\n")
    log.write('combinations: '+ str(combinations)+ "\nlength: "+ str(len(combinations)) + "\n")

    print('Thinking...')
    log.write("\n\n\n******************************\npermutation test\n*********************************\n")
    for gene in dictdict:
        true_scenario = compare.format_true_populations(true_lists, dictdict[gene])
        true_delta_fst = delta_fst_true(true_scenario)
        possible_scenarios = compare.format_populations(combinations, dictdict[gene])
        poss_delta_fsts = delta_fst_average(possible_scenarios)
        same_diff_true = true_fst_same_diff(true_scenario)
        p = calculate_p_value(true_delta_fst, poss_delta_fsts)
        this_gene = track_gene(gene, true_delta_fst, p, poss_delta_fsts)
        p_value = p[0]
        sig = "no"
        for value in this_gene:
            log.write('{0}\n'.format(value) + "\n")
        line = gene + ',' + str(p_value) + ',' + str(sig) +','+ str(same_diff_true[0]) +','+ str(same_diff_true[1]) + '\n'
        if p_value <= 0.05:
            sig = "yes"
#             this_gene.pop(3)
#             this_gene.pop(4)
#             this_gene.pop()
            line = gene + ',' + str(p_value) + ',' + str(sig) +','+ str(same_diff_true[0]) +','+ str(same_diff_true[1]) + '\n'

            for value in this_gene:
                results.write('{0}\n'.format(value))
            sig_output.write(line)
            all_output.write(line)
        else:
            line = gene + ',' + str(p_value) + ',' + str(sig) +','+ str(same_diff_true[0]) +','+ str(same_diff_true[1]) + '\n'
            all_output.write(line)
    log.close()
    results.close()
    sig_output.close()
    all_output.close()
    print("Finished! See sig_output.csv, all_output.csv, results.txt, and log.txt")

def track_gene(gene, true_delta_fst, p, poss_delta_fsts):
    '''
    This function constructs a list containing various pieces of
    information related to a gene's analysis results, such as the gene
    identifier, true delta fst, p-value, possible delta fsts, qualifiers, and
    total count. This function is used within the larger context to gather
    and organize information about genes during the analysis process.
    '''
    this_gene = []
    this_gene.append(gene)
    this_gene.append("True delta fst: " + str(true_delta_fst))
    this_gene.append("p-value: " + str(p[0]))
    this_gene.append("Possible delta fsts: " + str(poss_delta_fsts))
    this_gene.append("Qualifiers (those with delta fst ≥ true delta fst): " + str(p[1]))
    this_gene.append("Total: " + str(p[2]))
    this_gene.append("\n")
    #print("this_gene: ", this_gene)
    return this_gene



