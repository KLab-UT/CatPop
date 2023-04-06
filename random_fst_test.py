import random

def generate_random_numbers(amount):
    i = 0
    rand = ""
    while i < amount:
        rand = rand + str(round(random.uniform(0, 1.0), 4)) + ","
        i += 1
    return rand


def make_fst_file(length, number_of_genes):
    #make population_pairs
    populations = []
    population_pairs = ""
    for i in range(length):
        populations.append("Pop"+str(i+1))
    for count, i in enumerate(populations):
        for j in populations[count+1:]:
            population_pairs = population_pairs + ("Fst_"+i+"_"+j) + ","
    with open("random_fst_test.csv", "w") as rft:
        rft.write("geneID," + population_pairs)
        for i in range(number_of_genes):
            i = str(i+1)
            #make population_pairs and random fst's into a .csv file
            fsts = generate_random_numbers(len(population_pairs))
            rft.write("\ngene_"+ i + "," + fsts)

# make_fst_file(length_of_populations_list)
make_fst_file(8, 547)
