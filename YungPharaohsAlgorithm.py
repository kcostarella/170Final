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


    allSolutions = GenerateSolutions(InstanceSeed, ImproveSeed) #allSolutions is an dict with <solution,weight> pairs, where solution are solutions and weight is the 
    #associated weight of the solution

    #Picks the best solution
    currentBest = sys.maxint
    for solution, weight in allSolutions:
    	if weight < currentBest:
    		currentBest = weight
    		currentBestSolution = solution




    def GenerateSolutions(iSeed,uSeed):
    	"""Generates a dictionary of <solution,weight> pairs, where sollution is a solution to an instance of NTSP
    	and the weight value is the weight or cost associated with the given solution. iSeed is an integer that represents
    	the number of solution keys returned in the allSolutions dictionary. uSeed is another integer that represents 
    	how many iterations of updateSolution will be called per solution"""
    	allSolutions = {}
    	for i in range(0,iSeed):
    		solution,weight = GenerateSolution() #generates a random instance
    		for i in range(0,uSeed):
    			solution, weight = UpdateSolution(solution,weight) #hill climbing improvement algorithm
    		allSolutions[solution] = weight #adds the solution,weight pair to the allSolutions dict
    	return allSolutions

    def GenerateSolution():
   		"""Generates a completely random solution for the particular instance of NTSP"""
   		solution = []
    	totalWeight = 0 # the total weight of our answer
    	hasVisited = [False] * N
    	colorCount = [] #Color count is a 2 element array where colorCount[0] = currentColor and colorCount[1] = the number of times 
    	#We've seen the currentColor

		#Initilize (Pick a starting State)
		currentState = random.randint(0,N-1) #picks a random start position
		colorCount[0] = c[currentState] #Sets colorCount[0] to the color of the currentState...
		colorCount[1] = 1 #... and We've now seen this color once...
		hasVisited[currentState] = True #... and We've just visited this state...
		solution.append[currentState] #... and this state is part of our solution



		#Travel (Loops through the remaning N-1 cities)    	
    	for n in range(0,N-1):
    		prevState = currentState #saves the previous state
    		validMoves = GenerateValidPositions(hasVisted) #generates valid next moves determined by internal logic in GenerateValidPositions
    		currentState = validMoves[random.randint(0,len(validMoves)-1)] #assigns the currentState to a random state from the validMoves

    		totalWeight += d[prevState][currentState] #increments the total weight by the cost to travel form prevState to currentState
    		#updates the colorCount depending on the color of currentState
    		if colorCount[0] == c[currentState]:
    			colorCount[0] += 1
    		else:
    			colorCount[0] = c[currentState]
    			colorCount[0] = 1
    		hasVisited[currentState] = True #Visit the current state#
    		solution.append[currentState] #Add it to our solution#
    	return (solution,totalWeight) #Return the solution and the totalWeight associated with it

    def GenerateValidPositions(visited, colorCount):
    	""" returns an array containing the indices of valid states to visit, where when
    	visited[i] = False indicates that index i is a valid state to visit. """
    	validMoves = []
    	for state in range(0,visited):
    		if (!visited[state] and (colorCount[1] < 3 or colorCount[0] != c[state])) #A state is valid if it hasnt been visited yet AND either its only seen the current color 
				#once or twice OR the color of the next state is different than the current color
				validMoves.append(state)
		return validMoves

    def UpdateSolution(instance, weight):
    	return (instance, weight)



    hasVisited[currCity] = True 
    assign[counter] = currCity
    counter += 1