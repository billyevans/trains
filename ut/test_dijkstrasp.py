from unittest import TestCase

__author__ = 'billyevans'

from core.digraph import DiGraph, Edge
from core.dijkstrasp import DijkstraSP

class TestDijkstraSP(TestCase):

    def setUp(self):
        self.G = DiGraph()
        self.G.add_edge(Edge(0, 1, 5.0))
        self.G.add_edge(Edge(0, 4, 9.0))
        self.G.add_edge(Edge(0, 7, 8.0))
        self.G.add_edge(Edge(1, 2, 12.0))
        self.G.add_edge(Edge(1, 3, 15.0))
        self.G.add_edge(Edge(1, 7, 4.0))
        self.G.add_edge(Edge(2, 3, 3.0))
        self.G.add_edge(Edge(2, 6, 11.0))
        self.G.add_edge(Edge(3, 6, 9.0))
        self.G.add_edge(Edge(4, 5, 4.0))
        self.G.add_edge(Edge(4, 6, 20.0))
        self.G.add_edge(Edge(4, 7, 5.0))
        self.G.add_edge(Edge(5, 2, 1.0))
        self.G.add_edge(Edge(5, 6, 13.0))
        self.G.add_edge(Edge(7, 5, 6.0))
        self.G.add_edge(Edge(7, 2, 7.0))

    def test_dist_to(self):
        dsp = DijkstraSP(self.G, 0)

        self.assertEqual(0.0, dsp.dist_to(0))
        self.assertEqual(5.0, dsp.dist_to(1))
        self.assertEqual(14.0, dsp.dist_to(2))
        self.assertEqual(17.0, dsp.dist_to(3))
        self.assertEqual(9.0, dsp.dist_to(4))
        self.assertEqual(13.0, dsp.dist_to(5))
        self.assertEqual(25.0, dsp.dist_to(6))
        self.assertEqual(8.0, dsp.dist_to(7))

    def test_edge_to(self):
        dsp = DijkstraSP(self.G, 0)

        self.assertEqual(0, dsp.edge[1].source())
        self.assertEqual(5.0, dsp.edge[1].distance())

        self.assertEqual(5, dsp.edge[2].source())
        self.assertEqual(1.0, dsp.edge[2].distance())

        self.assertEqual(2, dsp.edge[3].source())
        self.assertEqual(3.0, dsp.edge[3].distance())

        self.assertEqual(0, dsp.edge[4].source())
        self.assertEqual(9.0, dsp.edge[4].distance())

        self.assertEqual(4, dsp.edge[5].source())
        self.assertEqual(4.0, dsp.edge[5].distance())

        self.assertEqual(2, dsp.edge[6].source())
        self.assertEqual(11.0, dsp.edge[6].distance())

        self.assertEqual(0, dsp.edge[7].source())
        self.assertEqual(8.0, dsp.edge[7].distance())


    def test_cycle(self):
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

        dsp = DijkstraSP(G, 'B')

        self.assertEqual(9.0, dsp.dist_to('B'))
