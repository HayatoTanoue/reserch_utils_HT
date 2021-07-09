import networkx as nx
import matplotlib.pyplot as plt
from reserch_utils_HT.src.plots.network_info import *


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
