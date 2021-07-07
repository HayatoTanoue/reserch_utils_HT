import networkx as nx

from reserch_utils_HT.src.network_image import *


def test_network_to_image():
    G = nx.barabasi_albert_graph(10, 2)
    assert network_to_image(G, sort=False)
    assert network_to_image(G, sort=True)
