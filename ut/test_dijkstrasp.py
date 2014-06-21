from unittest import TestCase

__author__ = 'billyevans'

from core.digraph import DiGraph, Edge

class TestDijkstraSP(TestCase):
        # test graph
    # AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    def SetUp(self):
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

    #def test_dist_to1(self):
     #   dist = DijkstraSP(self.G, 'A')
      #  self.fail()

    #def test_has_path_to(self):
     #   G = self.get_test_graph()
      #  self.fail()

    #def test_path_to(self):
     #   G = self.get_test_graph()
      #  self.fail()