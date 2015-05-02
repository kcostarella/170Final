import random

edges = [[] for i in range(24)]
nodes = []
color = ["R", "B"]

def gen_edges(numEdges):
    edges = [[] for i in range(numEdges)]
    for row in edges:
        for i in range(numEdges):
            row.append(0)
    for i in range(numEdges):
        for j in range(numEdges):
            if i == j:
                edges[i][j] = 0
            else: 
                weight = random.randint(0, 100)
                edges[i][j] = weight
                edges[j][i] = weight
    return edges

def gen_nodes(numEdges):
    for i in range(numEdges):
        nodes.append(0)
    for i in range(numEdges):
        nodes[i] = color[random.randint(0,1)]
    return nodes

def gen_instance(numEdges, fileName):
    fout = open(fileName, "w")
    edges = gen_edges(numEdges)
    nodes = gen_nodes(numEdges)
    fout.write(numEdges + "\n")
    for i in range(numEdges):
        for j in range(numEdges):
            if j != numEdges - 1:
                fout.write("%s " % str(edges[i][j]))
            else:
                fout.write("%s\n" % str(edges[i][j]))
    for color in nodes:
        fout.write("%s" % color)
    return
