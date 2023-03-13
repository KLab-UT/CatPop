#make fst file into dictionary
def Make_fst_dictionary(file_name):
    fst_list = []
    fst_dict = {}
    with open(file_name, "r") as fst_d:
        lines = fst_d.readlines()
        for line in lines:
            fst_list.append(line)
    population = fst_list[0].split(",")
    population = population[1:]
    fst = fst_list[1].split(",")
    fst = fst[1:]
    for i in range(len(population)):
        p = population[i].strip()
        f = fst[i].strip()
        fst_dict[p] = f
    return fst_dict
#Dictionary to get fst values from compared populations
def Get_fst(a, b, fst_dict): #a and b are 2 different populations being compared
    key1 = "Fst_"+a+"_"+b
    key2 = "Fst_"+b+"_"+a
    print(key1)
    print(key2)
    if key1 in fst_dict:
        fst = fst_dict[key1]
    if key2 in fst_dict:
        fst = fst_dict[key2]
    return fst

#Get average FST for same and different
def Same_fst_avg(listA, listB): #use twice for list A and list B
    fst_sum = 0
    lists = [listA, listB]
    for list in lists:
        for count, i in enumerate(list):
            for j in list[count+1:]:
                fst_sum += Get_fst(i, j)
    fst_avg = fst_sum/30
def Diff_fst_avg(listA, listB): # get fst of populations in different lists
    fst_sum = 0
    for i in listA:
        for j in listB:
            fst_sum += Get_fst(i, j)
    fst_avg = fst_sum/36

#fst_dictionary = Make_fst_dictionary("PracticeFstData_OneGene.csv")
#Get_fst("MER", "MAH", fst_dictionary)

