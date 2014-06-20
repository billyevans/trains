from unittest import TestCase

__author__ = 'billyevans'

from digraph import DiGraph, Edge
from algo import distance

class TestDistance(TestCase):

    # test graph
    # AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    def get_test_graph(self):
        G = DiGraph()
        G.add_edge(Edge('A', 'B', 5))
        G.add_edge(Edge('B', 'C', 4))
        G.add_edge(Edge('C', 'D', 8))
        G.add_edge(Edge('D', 'C', 8))
        G.add_edge(Edge('D', 'E', 6))
        G.add_edge(Edge('A', 'D', 5))
        G.add_edge(Edge('C', 'E', 2))
        G.add_edge(Edge('E', 'B', 3))
        G.add_edge(Edge('A', 'E', 7))
        return G

    def test_distance1(self):
        G = self.get_test_graph()
        self.assertEqual(9, distance(G, ['A', 'B', 'C']))

    def test_distance2(self):
        G = self.get_test_graph()
        self.assertEqual(5, distance(G, ['A', 'D']))

    def test_distance3(self):
        G = self.get_test_graph()
        self.assertEqual(13, distance(G, ['A', 'D', 'C']))

    def test_distance4(self):
        G = self.get_test_graph()
        self.assertEqual(22, distance(G, ['A', 'E', 'B', 'C', 'D']))

    def test_distance5(self):
        G = self.get_test_graph()
        self.assertEqual('NO SUCH ROUTE', distance(G, ['A', 'E', 'D']))