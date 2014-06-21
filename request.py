from core import algo

__author__ = 'billyevans'
__all__ = ["process"]

# request format :
# <cmd>(<arg1> <arg2> ...)
#
# possible requests
# distance with list of vertices
# trips_eq_stops with 3 args @source, @dest, @limit
# trips_le_stops with 3 args @source, @dest, @limit
# trips_lt_stops with 3 args @source, @dest, @limit
# trips_eq_distance with 3 args @source, @dest, @limit
# trips_le_distance with 3 args @source, @dest, @limit
# trips_lt_distance with 3 args @source, @dest, @limit
# shortest_path with 2 args @source and @dest

def distance_wrap(G, args):
    d = algo.distance(G, args)
    return d if d >= 0 else 'NO SUCH ROUTE'

def parse_trips_args(G, args):
    if len(args) != 3:
        raise ValueError("Wrong args count for trips " + str(args))
    (source, dest, limit) = args
    G.has_node(source)
    G.has_node(dest)
    l = int(limit)
    if l < 0:
        raise ValueError("Wrong limit for trips " + limit)
    return (source, dest, l)


def trips(G, args, name):
    (source, dest, limit) = parse_trips_args(G, args)
    filt_fn = getattr(algo, name)
    fn = filt_fn(dest, limit)
    algo.bfs(G, source, fn)
    return fn.count

def shortest_path_wrap(G, args):
    if len(args) != 2:
        raise ValueError("Wrong args count for shortest_path " + str(args))

    (source, dest) = args
    G.has_node(source)
    G.has_node(dest)
    dist = algo.shortest_path(G, source, dest)
    return dist if dist >= 0 else 'NO SUCH ROUTE'

def process(G, req):
    cmd, args = req.split('(')
    args = args.strip().rstrip()
    if args[-1] != ')':
        raise ValueError("Wrong format of line")
    args = args[:-1]
    vlist = args.split(' ')
    return {
        'distance': lambda G, vlist: distance_wrap(G, vlist),
        'trips_eq_stops': lambda G, vlist: trips(G, vlist, 'BfsEQStops'),
        'trips_le_stops': lambda G, vlist: trips(G, vlist, 'BfsLEStops'),
        'trips_lt_stops': lambda G, vlist: trips(G, vlist, 'BfsLTStops'),
        'trips_eq_distance': lambda G, vlist: trips(G, vlist, 'BfsEQDist'),
        'trips_le_distance': lambda G, vlist: trips(G, vlist, 'BfsLEDist'),
        'trips_lt_distance': lambda G, vlist: trips(G, vlist, 'BfsLTDist'),
        'shortest_path': lambda G, vlist: shortest_path_wrap(G, vlist)
    }.get(cmd)(G, vlist)
