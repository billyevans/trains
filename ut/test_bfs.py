from unittest import TestCase

__author__ = 'billyevans'

from core.digraph import DiGraph, Edge
from core.algo import bfs, BfsLEStops, BfsEQStops, BfsLTStops, BfsEQDist, BfsLTDist


class TestBfs(TestCase):
    # test graph
    # AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    def setUp(self):
        self.G = DiGraph()
        self.G.add_edge(Edge('A', 'B', 5))
        self.G.add_edge(Edge('B', 'C', 4))
        self.G.add_edge(Edge('C', 'D', 8))
        self.G.add_edge(Edge('D', 'C', 8))
        self.G.add_edge(Edge('D', 'E', 6))
        self.G.add_edge(Edge('A', 'D', 5))
        self.G.add_edge(Edge('C', 'E', 2))
        self.G.add_edge(Edge('E', 'B', 3))
        self.G.add_edge(Edge('A', 'E', 7))

    # from C to C, less 4 stops, same as test_bfs_6
    def test_bfs_less(self):
        fn = BfsLTStops('C', 4)
        bfs(self.G, 'C', fn)
        self.assertEqual(2, fn.count)

    # from A to C, not more 1 stops
    def test_bfs_empty(self):
        fn = BfsLEStops('C', 1)
        bfs(self.G, 'A', fn)
        self.assertEqual(0, fn.count)

    # from C to C, not more 3 stops
    def test_bfs_6(self):
        fn = BfsLEStops('C', 3)
        bfs(self.G, 'C', fn)
        self.assertEqual(2, fn.count)

    # from A to C, with exacly 4
    def test_bfs_7(self):
        fn = BfsEQStops('C', 4)
        bfs(self.G, 'A', fn)
        self.assertEqual(3, fn.count)

    # from A to C, with exacly 5
    def test_bfs_(self):
        fn = BfsEQStops('C', 5)
        bfs(self.G, 'A', fn)
        self.assertEqual(3, fn.count)

    # from C to C, with distance less that 30
    def test_bfs_10(self):
        fn = BfsLTDist('C', 30)
        bfs(self.G, 'C', fn)
        self.assertEqual(7, fn.count)

    # from A to D, with distance = 21
    def test_bfs_one(self):
        fn = BfsEQDist('D', 21)
        bfs(self.G, 'A', fn)
        self.assertEqual(1, fn.count)