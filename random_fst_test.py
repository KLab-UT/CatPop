import random

def generate_random_numbers(amount):
    i = 0
    rand = []
    while i < amount:
        rand.append(round(random.uniform(0, 1.0), 6))
        i += 1
    return rand

#make population list
def make_population_pairs(length):
    populations = []
    population_pairs = []
    for i in range(length):
        populations.append("POP"+str(i+1))
    for count, i in enumerate(populations):
        for j in populations[count+1:]:
            population_pairs.append("FST_"+i+"_"+j)

def make_fst_file(length):
    #make population_pairs
    populations = []
    population_pairs = []
    for i in range(length):
        populations.append("POP"+str(i+1))
    for count, i in enumerate(populations):
        for j in populations[count+1:]:
            population_pairs.append("FST_"+i+"_"+j)
    #make population_pairs and random fst's into a .csv file
    fsts = generate_random_numbers(len(population_pairs))
    with open("random_fst_test.csv", "w") as rft:
        rft.write("geneID," + str(population_pairs).strip("[]").replace("'", ""))
        rft.write("\ngene_1," + str(fsts).strip("[]"))

# make_fst_file(length_of_populations_list)
make_fst_file(8)
