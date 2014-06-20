from unittest import TestCase

import digraphio

__author__ = 'billyevans'


class TestParse_adjlist(TestCase):
    def test_parse_adjlist(self):
        text_graph = [
            "1 2 3.0",
            "2 3 4.1",
            "5 6 13",
            "A OtherCity 666"
        ]
        G = digraphio.parse_adjlist(text_graph)
        #self.assertEqual('Some stuff', "xx");

    def test_parse_adjlist_empty(self):
        G = digraphio.parse_adjlist([])

    def test_parse_adjlist_empty_line(self):
        text_graph = [ "", "1 2 3.1", "" ]
        G = digraphio.parse_adjlist(text_graph)
