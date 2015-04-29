T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline()) # N is the number of cities
    hasVisited = [False] * N
    d = [[] for i in range(N)] # creates an array of N empty arrays
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()] # fills up the all N arrarys in array d
    c = fin.readline() # c becomes a string of all of the colors (RBRBR etc.)

    assign = [0] * N # the answer array being instantiated to all zeros

    counter = 0
    currCity = 0
    totalWeight = 0
    hasVisited[currCity] = True
    assign[counter] = currCity
    counter += 1

    while counter != N:
        smallestWeight = float("inf")
        closestCity = 0
        for x in range(0, N):
            if not hasVisited[x] and d[currCity][x] < smallestWeight:
                smallestWeight = d[currCity][x]
                closestCity = x

        totalWeight += smallestWeight
        currCity = closestCity

        hasVisited[currCity] = True
        assign[counter] = currCity # find an answer, and put into assign

        counter += 1

    assign = map(lambda x : x + 1, assign)

    fout.write("%s\n" % " ".join(map(str, assign))) # writes assign (the answer) to answer.out
fout.close()