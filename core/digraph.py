__author__ = 'billyevans'

from collections import defaultdict

# Edge of DiGraph with positive weight
class Edge(object):
    def __init__(self, v, w, distance):
        self.v = v
        self.w = w
        self.d = float(distance)
        if self.d < 0:
            raise ValueError("Wrong value of distance")

    def source(self):
        return self.v

    def dest(self):
        return self.w

    def distance(self):
        return self.d


# digraph with Edge's in adjlist representation
class DiGraph(object):
    def __init__(self):
        self.adjlist = defaultdict(lambda: defaultdict(Edge))
        self.nodeslist = set()
        self.ed = 0

    def add_edge(self, e):
        self.adjlist[e.source()][e.dest()] = e
        self.nodeslist.add(e.dest())
        self.nodeslist.add(e.source())
        self.ed += 1

    def e(self):
        return self.ed
    # return number of vertices
    def v(self):
        return len(self.nodeslist)

    # return edges pointing from v
    def adj(self, v):
        self.has_node(v)
        return self.adjlist[v]

    # check @v node and raise RuntimeError if there is no that node in the graph
    def has_node(self, v):
        if v not in self.nodeslist:
            raise ValueError("There is no that node in the graph " + str(v))

    def edges(self):
        return self.adjlist.items()

    def edges_iter(self):
        return iter(self.adjlist.items())

    def nodes(self):
        return self.nodeslist

    # return -1 if there is no such path
    def dist(self, v, w):
        self.has_node(v)
        self.has_node(w)
        if self.adjlist[v].get(w) is None:
            return -1
        return self.adjlist[v][w].distance()