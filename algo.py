__author__ = 'billyevans'


# return distance or NO SUCH ROUTE if there is no direct path
def distance(G, list):
    d = 0
    if len(list) == 0:
        return d
    source = list.pop(0)
    for n in list:
        nd = G.dist(source, n)
        if nd < 0:
            return 'NO SUCH ROUTE'
        d += nd
        source = n

    return d
