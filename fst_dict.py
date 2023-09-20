def makeDict(filename):
    '''Parses through file input and converts it into a fst dictionary'''
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(",")
        keys = keys[1:]

        values = f.readline().strip().split(",")
        values = values[1:]
        mDict = dict(zip(keys, values))
        return mDict

if __name__ == "__main__":
    main()
