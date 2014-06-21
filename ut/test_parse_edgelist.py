from unittest import TestCase

from core.digraphio import parse_edgelist

__author__ = 'billyevans'


class TestParseEdgelist(TestCase):
    def test_parse_edgelist(self):
        text_graph = [
            "1 2 3.0",
            "2 3 4.1",
            "3 6 13",
            "3 7 8",
            "A OtherCity 666"
        ]
        G = parse_edgelist(text_graph)
        self.assertEqual(5, G.e())
        self.assertEqual(7, G.v())
        self.assertEqual(1, len(G.adj('1')))
        self.assertEqual(1, len(G.adj('2')))
        self.assertEqual(2, len(G.adj('3')))
        self.assertEqual(0, len(G.adj('OtherCity')))

    def test_parse_edgelist_empty(self):
        G = parse_edgelist([])
        self.assertEqual(0, G.e())
        self.assertEqual([], G.edges())

    def test_parse_edgelist_empty_line(self):
        text_graph = ["", "1 2 3.1", ""]
        G = parse_edgelist(text_graph)
        self.assertEqual(1, G.e())
        self.assertEqual(2, G.v())
        self.assertEqual(1, len(G.adj('1')))
        self.assertEqual(0, len(G.adj('2')))

    def test_parse_edgelist_wrong_format(self):
        text_graph = ["1 2 3.0", "1 2 3.1 18"]
        self.assertRaises(TypeError, parse_edgelist, text_graph)

    def test_parse_edgelist_wrong_weight(self):
        text_graph = ["1 2 13asdasdXXX"]
        self.assertRaises(ValueError, parse_edgelist, text_graph)