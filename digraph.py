__author__ = 'billyevans'

from collections import defaultdict

class Edge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = float(weight)
        if self.weight < 0:
            raise TypeError("Wrong value of weight")


    def source(self):
        return self.v

    def dest(self):
        return self.w


# digraph with adj
class DiGraph(object):
    def __init__(self):
        self.adjlist = defaultdict(lambda: defaultdict(Edge))
        self.nodes = set()
        self.ed = 0

    def add_edge(self, e):
        self.adjlist[e.source()][e.dest()] = e
        self.nodes.add(e.dest())
        self.nodes.add(e.source())
        self.ed += 1

    def e(self):
        return self.ed
    # return number of vertices
    def v(self):
        return len(self.nodes)

    # return edges pointing from v
    def adj(self, v):
        if v not in self.nodes:
            raise RuntimeError("There is no that node in the graph " + str(v))
        return self.adjlist[v]

    def edges(self):
        return self.adjlist.items()

    def edges_iter(self):
        return iter(self.adjlist.items())

    # return -1 if there is no such path
    def dist(self, v, w):
        if v not in self.nodes:
            raise RuntimeError("There is no that node in the graph " + str(v))
        if w not in self.nodes:
            raise RuntimeError("There is no that node in the graph " + str(w))
        if self.adjlist[v].get(w) is None:
            return -1
        return self.adjlist[v][w].weight