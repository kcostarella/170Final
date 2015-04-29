T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline()) # N is the number of cities
    print(N)
    d = [[] for i in range(N)] #c reates an array of N empty arrays
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()] # fills up the all N arrarys in array d
    c = fin.readline() # c becomes a string of all of the colors (RBRBR etc.)

    # find an answer, and put into assign
    assign = [0] * N
    for i in xrange(N):
        assign[i] = i+1

    fout.write("%s\n" % " ".join(map(str, assign))) # writes assign (the answer) to answer.out
fout.close()