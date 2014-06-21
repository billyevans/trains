__author__ = 'billyevans'


# return distance or -1 if there is no direct path
def distance(G, list):
    d = 0
    if len(list) == 0:
        return d
    source = list.pop(0)
    for n in list:
        nd = G.dist(source, n)
        if nd < 0:
            return -1
        d += nd
        source = n

    return d

# iterate through the digraph @G, starting from @s
# without detecting cycles
# uses @cond for stopping
# if @cond returns False, then bfs doesn't go next on this vertex
# this algorithm could be easily extended by @cond
def bfs(G, s, cond):
    q = list()
    q.append((s, 0, 0))
    while len(q) > 0:
        (v, stops, dist) = q.pop(0)
        if cond(v, stops, dist) is False:
            continue
        for w in G.adj(v):
            q.append((w, stops+1, dist + G.dist(v, w)))


# helpers for @cond in bfs
# @dest and @num must be valid, eg @dest in the graph and @num > 0
# validation must provide users code, which are connected with graph
# <= @num stops
class BfsLEStops(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.stops = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops > 0:
            self.count += 1
        return (stops < self.stops)

# == @num stops
class BfsEQStops(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.stops = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops == self.stops:
            self.count += 1
        return (stops < self.stops)

# < @num stops
class BfsLTStops(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.stops = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops > 0:
            self.count += 1
        return (stops < self.stops-1)

# helpers with limitation in distance
# <= @num dist
class BfsLEDist(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.dist = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops > 0 and dist <= self.dist:
            self.count += 1
        return (dist <= self.dist)

# == @num dist
class BfsEQDist(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.dist = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops > 0 and dist == self.dist:
            self.count += 1
        return (dist <= self.dist)

# < @num dist
class BfsLTDist(object):
    def __init__(self, dest, num):
        self.dest = dest
        self.dist = num
        self.count = 0

    def __call__(self, v, stops, dist):
        if v == self.dest and stops > 0 and dist < self.dist:
            self.count += 1
        return (dist < self.dist)

# return shortest dist from @source to @dest
# if there is no route return -1
def shortest_path(G, source, dest):
    from dijkstrasp import DijkstraSP
    dsp = DijkstraSP(G, source)
    return dsp.dist_to(dest) if dsp.has_path_to(dest) else -1