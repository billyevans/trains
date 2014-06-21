from unittest import TestCase

__author__ = 'billyevans'

from core.digraphio import generate_adjlist
from core.digraph import DiGraph, Edge


class TestGenerateAdjlist(TestCase):
    def test_generate_adjlist_empty(self):
        G = DiGraph()
        for line in generate_adjlist(G):
            self.fail()

    def test_generate_adjlist_simple(self):
        G = DiGraph()
        G.add_edge(Edge(1, 2, 13))
        G.add_edge(Edge(1, 3, 666.1))

        orig = ["1 3 666.1", "1 2 13.0"]
        lines = []
        for line in generate_adjlist(G):
            lines.append(line)

        self.assertEqual(sorted(orig), sorted(lines))

    def test_generate_adjlist(self):
        G = DiGraph()
        G.add_edge(Edge(1, 2, 3.0))
        G.add_edge(Edge(2, 3, 4.1))
        G.add_edge(Edge(3, 6, 13))
        G.add_edge(Edge(3, 7, 8))
        G.add_edge(Edge('A', 'OtherCity', '666'))

        orig = [
            "1 2 3.0",
            "2 3 4.1",
            "3 6 13.0",
            "3 7 8.0",
            "A OtherCity 666.0"
        ]
        lines = []
        for line in generate_adjlist(G):
            lines.append(line)

        self.assertEqual(sorted(orig), sorted(lines))