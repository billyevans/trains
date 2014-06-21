Trains
=========

Solution for trains problem, written in python



Usage
----
I use external library for rbtree, which I need in Dijkstra's algorithm implementation.
Install it
```sh
sudo easy_install rbtree
```
Now we can launch trains.py
```sh
./trains.py graph.txt req.txt out.txt
```

Contents
----

* trains.py - main program, has 3 arguments <graph-file> <requests-file> <output-file>
* run_ut.py - launcher for all unit tests in ut/ folder
* graph.txt - graph example file
* req.txt - requests example file
* request.py - little helper with user-requests handling
* ut/* - tests for most functionality
* core/algo.py - implementation of distance(), bfs() traverse and shortest_path() - just wrapper for Dijkstra's algorithm usage
* core/digraph.py - simplest DiGraph and it's Edge implementation
* core/digraphio.py - functions for reading/writing graph from/to text representation
* core/dijkstrasp.py - Dijkstra's algorithm implementation

Format of input files
----

<graph-file> must be in edge list format, such as
```
<source> <destanation> <distance>
...
```
<requests-file> must be in format
```
<cmd>(<arg1> <arg2> ...)
...
```
Availiable commands in request file
--
- distance with list of vertices
- trips_eq_stops with 3 args @source, @dest, @limit
- trips_le_stops with 3 args @source, @dest, @limit
- trips_lt_stops with 3 args @source, @dest, @limit
- trips_eq_distance with 3 args @source, @dest, @limit
- trips_le_distance with 3 args @source, @dest, @limit
- trips_lt_distance with 3 args @source, @dest, @limit
- shortest_path with 2 args @source and @dest