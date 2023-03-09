#Dictionary to get fst values from compared populations
def Get_fst(a, b): #a and b are 2 different populations being compared
	print("put dictionary here")
	print("return fst")
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

