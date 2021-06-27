import unittest

from graph_solution import Graph

class TestGraph(unittest.TestCase):
    
    def tests(self):

        GRAPH = Graph()
        for node in ['a', 'b', 'c', 'd']:
            GRAPH.add_vertex(node)

        for edge in [('a', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'd')]:
            GRAPH.add_edge(edge)

        GRAPH.add_vertex('e')
        self.assertEqual(GRAPH.graph, {'a': ['b', 'c', 'd'], 'b': ['a'], 'c': ['a', 'd'], 'd': ['a', 'c'], 'e': []})
        GRAPH.add_edge(('d', 'e'))
        self.assertEqual(GRAPH.graph, {'a': ['b', 'c', 'd'], 'b': ['a'], 'c': ['a', 'd'], 'd': ['a', 'c', 'e'], 
        'e': ['d']})
        self.assertEqual(GRAPH.get_neighbors('a'), ['b', 'c', 'd'])
        self.assertEqual(GRAPH.get_incident_edges('a'), [('a', 'b'), ('a', 'c'), ('a', 'd')])
        self.assertEqual(GRAPH.is_reachable('b', 'd'), True)


unittest.main()