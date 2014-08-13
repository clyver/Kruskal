__author__ = 'christopherlyver'
from Node import Node
from Graph import Graph

nodeA = Node('A', [['B', 1], ['C', 3]])
nodeB = Node('B', [['A', 1], ['C', 2]])
nodeC = Node('C', [['A', 3], ['B', 2]])
nodeD = Node('D', [['C', 4], ['A', 5], ['B', 3]])

nodes = [nodeA, nodeB, nodeC, nodeD]

graph = Graph(nodes)

size = graph.size()
edges = graph.get_edges()
sorted_edges = graph.sort_edges()
kruskal = graph.kruskal()
len_kruskal = len(kruskal)
print "all edges: " , edges
print "sorted edges:", sorted_edges
print "kruskal:", kruskal
