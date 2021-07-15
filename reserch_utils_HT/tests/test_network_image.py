import os
import networkx as nx

from reserch_utils_HT.src.network_image import *


def test_network_to_image():
    G = nx.barabasi_albert_graph(10, 2)
    assert network_to_image(G, sort=False)

    # sort
    assert network_to_image(G, sort=True)
    # shuffle
    assert network_to_image(G, shuffle=True)

    img1 = network_to_image(G, shuffle=True, seed=10)
    img2 = network_to_image(G, shuffle=True, seed=10)
    assert img1 == img2


def test_image_to_network():
    origin = nx.barabasi_albert_graph(100, 2, seed=10)
    img = network_to_image(origin)
    img.save("BA_m2_seed10.png")

    img = network_to_image(origin, sort=True)
    img.save("BA_sort_m2_seed10.png")

    G = image_to_network("BA_m2_seed10.png")
    G_sort = image_to_network("BA_sort_m2_seed10.png")

    assert nx.number_of_edges(G) == nx.number_of_edges(origin)
    assert nx.number_of_edges(G_sort) == nx.number_of_edges(origin)

    assert nx.is_isomorphic(G, origin)
    assert nx.is_isomorphic(G, G_sort)
    assert nx.is_isomorphic(origin, G_sort)

    os.unlink("BA_m2_seed10.png")
    os.unlink("BA_sort_m2_seed10.png")

    origin = nx.barabasi_albert_graph(1000, 2, seed=1)
    img = network_to_image(origin)
    img.save("BA1000_m2_seed1.png")
    img = network_to_image(origin, sort=True)
    img.save("BA1000_sort_m2_seed1.png")

    G = image_to_network("BA1000_m2_seed1.png")
    G_sort = image_to_network("BA1000_sort_m2_seed1.png")

    assert nx.number_of_edges(G) == nx.number_of_edges(origin)
    assert nx.number_of_edges(G_sort) == nx.number_of_edges(origin)

    os.unlink("BA1000_m2_seed1.png")
    os.unlink("BA1000_sort_m2_seed1.png")
