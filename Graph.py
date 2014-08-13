__author__ = 'christopherlyver'

class Graph():
    """
    A class representation of a graph composed of a list off Nodes()
    """

    def __init__(self, nodes):
        """
        @param nodes: A list of all nodes in the graph
        """
        self.nodes = nodes

    def get_edges(self):
        """
        Get all the edges in the graph without duplicates
        ex. we don't want [ (('A', 'B'), 1), (('B', 'A'), 1)) ]
        """
        all_edges = []

        # Gather all the edges in the graph, and don't revisit seen paths
        for node in self.nodes:
            for edge in node.neighbors:
                size = len(all_edges)
                i = 0
                duplicate = False
                while i < size:
                    if set([node.name, edge[0]]) in all_edges[i]:
                        duplicate = True
                        i += 1
                    else:
                        i += 1
                if not duplicate:
                    all_edges.append([set([node.name, edge[0]]), edge[1]])

        return all_edges

    def sort_edges(self):
        # The edges of the graph sorted by their weights
        edges = self.get_edges()
        edges.sort(key=lambda x: x[1])
        return edges

    def size(self):
        # The number of nodes in the graph
        return len(self.nodes)

    def kruskal(self):

        edges = self.sort_edges()
        graph_size = self.size()
        visited_nodes = set()
        # Minimum Spanning Tree
        mst = []

        i = 0
        # We stop when we take in N-1 edges
        while len(mst) != graph_size-1:

            # Iterate through all the edges
            edge = edges[i]

            # Determine if the current edge creates a loop
            creates_loop = edge[0].issubset(visited_nodes)

            # If this edge doesn't create a loop, we accept it
            if not creates_loop:
                mst.append(edge)
                visited_nodes = (visited_nodes | edge[0])
                i += 1
            # If it doesn't, we increment i and move on to the next edge
            else:
                i += 1
        return mst
