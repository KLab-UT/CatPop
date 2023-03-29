def make_dict_dict(filename):
    f=open(filename, "r")
    first=f.readline()
    popComb=first.strip().split(",")[1:]
    for line in f:
        geneID=line.strip().split(",")[:1]
        fsts=line.strip().split(",")[1:]
        dict_popComb={popComb[0]:fsts[0]}
        for i in range(1,len(popComb)):
            dict_popComb[popComb[i]]=fsts[i]
        dict_geneID={geneID[0]:dict_popComb}
    return dict_geneID
