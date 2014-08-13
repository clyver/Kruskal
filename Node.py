__author__ = 'christopherlyver'

class Node():

    """
    The class representation of a node.  Will be a component of a higher-level graph.
    @param name = string of the node's name   ex. 'Node A'
    @param neighbors =  array of tuples of the node's neighbors with distance    ex. [('nodeA', 5)...]
    """

    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

