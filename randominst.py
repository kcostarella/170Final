import random

edges = [[] for i in range(24)]
nodes = []
color = ["R", "B"]

def gen_edges():
    for row in edges:
        for i in range(24):
            row.append(0)
    for i in range(24):
        for j in range(24):
            if i == j:
                edges[i][j] = 0
            else: 
                weight = random.randint(0, 100)
                edges[i][j] = weight
                edges[j][i] = weight
    return edges

def gen_nodes():
    for i in range(24):
        nodes.append(0)
    for i in range(24):
        nodes[i] = color[random.randint(0,1)]
    return nodes

def gen_instance():
    fout = open("gkj1.in", "w")
    edges = gen_edges()
    nodes = gen_nodes()
    fout.write("24\n")
    for i in range(24):
        for j in range(24):
            if j != 23:
                fout.write("%s " % str(edges[i][j]))
            else:
                fout.write("%s\n" % str(edges[i][j]))
    for color in nodes:
        fout.write("%s" % color)
    return
