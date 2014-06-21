from unittest import TestCase

__author__ = 'billyevans'

from core.digraph import DiGraph, Edge
from core.algo import distance

class TestDistance(TestCase):

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

    def test_distance0(self):
        self.assertEqual(0, distance(self.G, []))

    def test_distance01(self):
        self.assertEqual(0, distance(self.G, ['E']))

    def test_distance1(self):
        self.assertEqual(9, distance(self.G, ['A', 'B', 'C']))

    def test_distance2(self):
        self.assertEqual(5, distance(self.G, ['A', 'D']))

    def test_distance3(self):
        self.assertEqual(13, distance(self.G, ['A', 'D', 'C']))

    def test_distance4(self):
        self.assertEqual(22, distance(self.G, ['A', 'E', 'B', 'C', 'D']))

    def test_distance5(self):
        self.assertEqual(-1, distance(self.G, ['A', 'E', 'D']))