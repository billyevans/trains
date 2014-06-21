__author__ = 'billyevans'

import rbtree

# implementation with rbtree instead priority_queue, which are a little worse that PQ
# but there is no PQ for python with another indexation by value in it, which are necessary for that implementation
# for best solution I have to implement it

# TODO: make good priority_queue

class DijkstraSP(object):
    # Computes a shortest paths tree from @s to every other vertex in @G
    def __init__(self, G, s):
        self.dist = dict(map(lambda a: (a, float("inf")), G.nodes()))
        self.dist[s] = 0.0
        self.edge = dict()
        self.G = G

        # relax vertices in order of distance from s
        self.pq = rbtree.rbtree()
        #self.entry_finder = set()

        # we need to maintain both
        self.pq[(self.dist[s], s)] = s
        #self.entry_finder.add(s)
        while len(self.pq) > 0:
            v = self.pq.pop()
            #self.entry_finder.remove(v)
            for e in G.adj(v):
                self._relax(v, e)

    # relax edge e and update pq if changed
    def _relax(self, v, w):
        dist = self.G.dist(v, w)
        if self.dist[w] > self.dist[v] + dist:
            old = self.dist[w]
            self.dist[w] = self.dist[v] + dist
            self.edge[w] = self.G.adj(v)[w]
            #if w in self.entry_finder:
            if (old, w) in self.pq:
                del self.pq[(old, w)]
            self.pq[(self.dist[w], w)] = w
           # else:
           #     self.pq[(self.dist[w], w)] = w
            #    self.entry_finder.add(w)

    def dist_to(self, v):
        return self.dist[v]

    def has_path_to(self, v):
        return self.dist[v] < float("inf")

    def path_to(self, v):
        path = set()
        if self.has_path_to(v) is False:
            return path
        e = self.edge.get(v)
        while e is not None:
            path.add(e)
            e = self.edge.get(e.source())

        return path
