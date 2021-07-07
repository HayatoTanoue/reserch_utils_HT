import networkx as nx

from reserch_utils_HT.src.network_model.ba_base import *


def test_no_preferential_attachment():
    G = no_preferential_attachment(100, 2, seed=10)
    assert len(G) == 100
    # エッジ数が正しいかどうか
    assert G.number_of_edges() == (98 * 2)

    # seed が同じ時に同型かどうか
    G1 = no_preferential_attachment(100, 2, seed=10)
    assert nx.is_isomorphic(G, G1)


def test_no_growth():
    G = no_growth(100, 198, seed=10)
    assert len(G) == 100
    assert G.number_of_edges() == 192

    # seed が同じ時に同型かどうか
    G1 = no_growth(100, 198, seed=10)
    assert nx.is_isomorphic(G, G1)
