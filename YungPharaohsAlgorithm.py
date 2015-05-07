import random

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
 	
    InstanceSeed = 5 #how instances to generate
    UpdateSeed = 4 #how many improvement update steps are taken

    allSolutions = GenerateSolution(InstanceSeed, ImproveSeed) #allSolutions is an dict with <assign,weight> pairs, where assign are solutions and weight is the 
    #associated weight of the solution

    #Picks the best solution
    currentBest = sys.maxint
    for solution, weight in allSolutions:
    	if weight < currentBest:
    		currentBest = weight
    		currentBestSolution = solution




    def GenerateSolution(iSeed,uSeed): #Generates the solution... yay abstraction
    	allSolutions = {}
    	for i in range(0,iSeed):
    		instance,weight = GenerateInstance() #generates a random instance
    		for i in range(0,uSeed):
    			instance, weight = UpdateInstance(instance,weight) #hill climbing improvement algorithm
    		allSolutions[instance] = weight
    	return allSolutions

    def GenerateInstance():
    	assign = [0] * N # the answer array being instantiated to all zeros/ path taken

    	return 0

    def UpdateInstance(instance, weight):
    	return (0,0)



    hasVisited[currCity] = True 
    assign[counter] = currCity
    counter += 1