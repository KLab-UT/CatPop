import json

def make_dict_dict(filename):
    f=open(filename, "r")
    first=f.readline()
    popComb=first.strip().split(",")[1:] #make list of population combinations
    dict_geneID={}
    for line in f:
        geneID=line.strip().split(",")[:1]  #get geneID which is the first element in the line
        fsts=line.strip().split(",")[1:]  #get fst values which are the rest of the elements in the line 
        dict_popComb={popComb[0]:fsts[0]}
        for i in range(1,len(popComb)):
            dict_popComb[popComb[i]]=fsts[i]
        dict_geneID[geneID[0]] = dict_popComb
    return dict_geneID

with open ('geneID_dictionary.json', 'w') as gd:
    json.dumps(make_dict_dict("exons.popgen.csv"))

#with open('geneID_dictionary.json') as json_file:
#    dict_geneID = json.load(json_file)
