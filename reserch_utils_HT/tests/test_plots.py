import networkx as nx
import matplotlib.pyplot as plt
from reserch_utils_HT.src.plots.network_info import *
from reserch_utils_HT.src.plots.draw_network import *


def test_degree_hist():
    G = nx.barabasi_albert_graph(100, 2)
    fig, ax = plt.subplots()
    degree_hist(G)

    fig, ax = plt.subplots()
    degree_hist(G, ax)

    fig, ax = plt.subplots()
    degree_hist(G, ax, log=True)


def test_degree_correlation():
    G = nx.barabasi_albert_graph(100, 2, seed=10)
    fig, ax = plt.subplots()
    degree_correlation(G, ax)
    degree_correlation(G, average=True)


def test_draw_origin():
    G = nx.barabasi_albert_graph(100, 2, seed=10)
    # default plot
    draw_origin(G)
    # ax
    fig, ax = plt.subplots()
    draw_origin(G, ax=ax)
    # change parameter
    fig, ax = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    draw_origin(
        G,
        pos=pos,
        ax=ax,
        k=1,
        node_alpha=0.5,
        node_mag=100,
        node_cmap=plt.cm.jet,
        edge_alpha=0.3,
        label=False,
        cbar=False,
    )


def test_plot_subgraph():
    G = nx.barabasi_albert_graph(100, 2, seed=10)

    plot_subgraph(G, range(10))

    fig, ax = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    plot_subgraph(G, [5, 99], ax=ax, pos=pos, main_c="y", sub_c="b")
