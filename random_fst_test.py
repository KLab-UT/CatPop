import random
import get_all_combinations as gac

def generate_random_numbers(amount):
    i = 0
    rand = []
    while i < amount:
        rand.append(round(random.uniform(0, 1.0), 6))
        i += 1
    return rand
        
generate_random_numbers(10)

#make population list
length = 10
populations = []
population_pairs = []
for i in range(length):
    populations.append("POP"+str(i+1))
for count, i in enumerate(populations):
    for j in populations[count+1:]:
        population_pairs.append("FST_"+i+"_"+j)

def make_fst_file(population_pairs):
    fsts = generate_random_numbers(len(population_pairs))
    with open("random_fst_test.txt", "w") as rft:
        rft.write("geneID: " + str(population_pairs).strip("[]"))
        rft.write("\ngene_1: " + str(fsts).strip("[]"))
        
    #write geneID + population_pairs to fst_file
    #write gene1 + random fst values to fst_file 

make_fst_file(population_pairs)
# with open("random_fst_test.txt", "w") as rft:
#     rft.write("geneID: ")