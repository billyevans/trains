__author__ = 'billyevans'


"class DiEdge(Object):"

class Edge(Object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    def from(self):
        return self.v



class DiGraph(Object):
    def __init__(self):
        self.adj = {}

