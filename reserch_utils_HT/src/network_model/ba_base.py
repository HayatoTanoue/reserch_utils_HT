import networkx as nx
import numpy as np


__all__ = ["no_preferential_attachment", "no_growth"]


def no_preferential_attachment(n, m, seed=None, initial_graph=None):
    """
    優先的選択がないバラバシアルバートグラフ

    network science chapter5.6 model A

    Parameters
    ----------
    n : int
        number of nodes.
    m : int
        number of add node edge.
    seed : int
        numpy random seed (default=None)
    initial_graph : network graph
        Initial network

    Returns
    -------
    G : networkx graph

    """
    if seed:
        np.random.seed(seed)

    if initial_graph is None:
        G = nx.empty_graph(m)  # generate m nodes empty graph
    else:
        G = initial_graph.copy()

    source = len(G)

    for _ in range(n - source):
        nodes = list(G.nodes())
        new_node = nodes[-1] + 1
        G.add_node(new_node)

        selected = np.random.choice(nodes, size=m, replace=False)

        G.add_edges_from([(new_node, select) for select in selected])

    return G


def no_growth(n, step, seed=None):
    """
    成長のないバラバシアルバートグラフ

    network science chapter5.6 model B

    Parameters
    ----------
    n : int
        number of nodes.
    step : int
        number of steps.
    seed : int
        numpy random seed (default=None)

    Returns
    -------
    G : networkx graph
    """
    if seed:
        np.random.seed(seed)

    G = nx.empty_graph(n)  # generate n nodes empty graphe

    deg_list = np.ones(n)
    nodes = range(n)

    start_nodes = np.random.choice(nodes, size=step)

    for start in start_nodes:
        p = deg_list / sum(deg_list)
        selected = np.random.choice(nodes, size=1, p=p)
        while start == selected:
            selected = np.random.choice(nodes, size=1, p=p)
        deg_list[start] += 1
        deg_list[selected] += 1

        G.add_edge(start, selected[0])
    return G