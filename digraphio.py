__author__ = 'billyevans'

__all__ = ['parse_adjlist']


def parse_adjlist(lines):
    G=DiGraph()
    for line in lines:
        if not len(line):
            continue
        vlist = line.strip().split(' ')

        if len(vlist) != 3:
            raise TypeError("Wrong line with edge of DiGraph")
        v = vlist[0]
        w =  vlist[1]
        weight = vlist[2]
        if weight < 0:
            raise TypeError("Negative weight of route")
        G.add_edge(Edge(v, w, weight))
        print(w, v, weight)





#def generate_adjlist(G):

