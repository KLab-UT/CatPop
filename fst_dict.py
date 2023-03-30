'''functions for parsing through file input and converting it into a fst dictionary'''

def makeDict(filename):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]

        values = f.readline().strip().split(",")
        values = values[1:]
        mDict = dict(zip(keys, values))
        return mDict