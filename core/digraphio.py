__author__ = 'billyevans'

from core.digraph import DiGraph, Edge

def parse_adjlist(lines):
    G = DiGraph()
    for line in lines:
        if not len(line):
            continue
        vlist = line.strip().split(' ')
        if len(vlist) != 3:
            raise TypeError("Wrong line with edge of DiGraph")
        v = vlist[0]
        w = vlist[1]
        weight = vlist[2]
        G.add_edge(Edge(v, w, weight))

    return G

def generate_adjlist(G):
    for s, nbrs in G.edges_iter():
        for t, data in nbrs.items():
            #line = '(' + str(s) + ' -> ' + str(t) + ') ' + str(data.weight)
            line = str(s) + ' ' + str(t) + ' ' + str(data.distance())
            yield line
