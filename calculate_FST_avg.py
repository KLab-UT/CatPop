#make fst file into dictionary
def Make_fst_dictionary(file_name):
    fst_list = []
    fst_dict = {}
    with open(file_name, "r") as fst_d:
        lines = fst_d.readlines()
        for line in lines:
            fst_list.append(line)
    population = fst_list[0].split(",")
    population = population[1:]  #removes the first thing in the line that is not a population
    fst = fst_list[1].split(",")
    fst = fst[1:]  #removes the first thing in the line that is not aN FST value
    for i in range(len(population)):
        p = population[i].strip()
        f = fst[i].strip()
        fst_dict[p] = f
    return fst_dict
#Dictionary to get fst values from compared populations
def Get_fst(a, b, fst_dict): #a and b are 2 different populations being compared
    key1 = "Fst_"+a+"_"+b
    key2 = "Fst_"+b+"_"+a
    if key1 in fst_dict:
        fst = fst_dict[key1]
    if key2 in fst_dict:
        fst = fst_dict[key2]
    return fst

#Get average FST for same and different
def Same_fst_avg(list_a, list_b, fst_dict): #use twice for list A and list B
    fst_sum = 0.0
    lists = [list_a, list_b]
    for li in lists:
        for count, i in enumerate(li):
            for j in li[count+1:]:
                fst = Get_fst(i, j, fst_dict)
                fst_sum += float(fst)
    fst_avg = fst_sum/30
    return fst_avg
def Diff_fst_avg(list_a, list_b, fst_dict): # get fst of populations in different lists
    fst_sum = 0.0
    for i in list_a:
        for j in list_b:
            fst = Get_fst(i, j, fst_dict)
            fst_sum += float(fst)
    fst_avg = fst_sum/36
    return fst_avg

#fst_dictionary = Make_fst_dictionary("PracticeFstData_OneGene.csv")
#Get_fst("MER", "MAH", fst_dictionary)

