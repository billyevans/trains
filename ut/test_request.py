from unittest import TestCase

__author__ = 'billyevans'

import request
from core.digraph import DiGraph, Edge

class TestRequest(TestCase):
    def setUp(self):
        self.G = DiGraph()
        self.G.add_edge(Edge('1', '2', 5))
        self.G.add_edge(Edge('2', '3', 2))
        self.G.add_edge(Edge('1', '3', 8))

    def test_request_empty(self):
        self.assertRaises(ValueError, request.process, self.G, '')

    def test_request_not_cmd(self):
        self.assertRaises(ValueError, request.process, self.G, 'asdads 123')

    def test_request_wrong_format(self):
        self.assertRaises(ValueError, request.process, self.G, 'distance(1 2 3')

    def test_request_wrong_cmd(self):
        self.assertRaises(TypeError, request.process, self.G, 'distance2(1 2 3)')


    # simple test all commands
    # dist
    def test_request_dist_wrong_vert1(self):
        self.assertRaises(ValueError, request.process, self.G, 'distance(X 3)')

    def test_request_distance1(self):
        self.assertEqual(8, request.process(self.G, 'distance(1 3)'))

    def test_request_distance1(self):
        self.assertEqual(7, request.process(self.G, 'distance(1 2 3)'))

    def test_request_distance2(self):
        self.assertEqual('NO SUCH ROUTE', request.process(self.G, 'distance(3 1)'))
    # trips
    def test_request_trips_wrong_vert1(self):
        self.assertRaises(ValueError, request.process, self.G, 'trips_eq_stops(X 3 2)')

    def test_request_trips_wrong_limit1(self):
        self.assertRaises(ValueError, request.process, self.G, 'trips_eq_stops(1 3 -2)')

    def test_request_trips_wrong_limit2(self):
        self.assertRaises(ValueError, request.process, self.G, 'trips_eq_stops(1 3 XXX)')

    def test_trips_trips_wrong_arg_num1(self):
        self.assertRaises(ValueError, request.process, self.G, 'trips_eq_stops(1 2 160 100)')

    def test_trips_trips_wrong_arg_num2(self):
        self.assertRaises(ValueError, request.process, self.G, 'trips_eq_stops(1 2)')

    def test_trips_eq_stops(self):
        self.assertEqual(1, request.process(self.G, 'trips_eq_stops(1 3 2)'))

    def test_trips_le_stops(self):
        self.assertEqual(2, request.process(self.G, 'trips_le_stops(1 3 2)'))

    def test_trips_lt_stops(self):
        self.assertEqual(1, request.process(self.G, 'trips_lt_stops(1 3 2)'))

    def test_trips_eq_distance(self):
        self.assertEqual(1, request.process(self.G, 'trips_eq_distance(1 3 7)'))

    def test_trips_le_distance(self):
        self.assertEqual(2, request.process(self.G, 'trips_le_distance(1 3 8)'))

    def test_trips_lt_distance(self):
        self.assertEqual(1, request.process(self.G, 'trips_lt_distance(1 2 160)'))

    # shoretest path
    def test_sp_wrong_arg_num1(self):
        self.assertRaises(ValueError, request.process, self.G, 'shortest_path(1 2 160)')

    def test_sp_wrong_arg_num2(self):
        self.assertRaises(ValueError, request.process, self.G, 'shortest_path(1)')

    def test_sp_simple(self):
        self.assertEqual(7, request.process(self.G, 'shortest_path(1 3)'))

    def test_sp_simple(self):
        self.assertEqual('NO SUCH ROUTE', request.process(self.G, 'shortest_path(3 1)'))