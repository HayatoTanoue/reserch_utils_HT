import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt

__all__ = ["degree_hist", "degree_correlation"]


def degree_hist(G, ax=None, log=False, bins=50, alpha=1, color="r", label=None):
    """次数分布を作成

    Parameter
    ----------
    G : networkx graph
    ax : matplotlib axes (グラフの描画先)
    log : bool
        対数グラフにするか (default = False)
    bins : int
        ヒストグラムの階級数
    """

    if ax is None:
        fig, ax = plt.subplots()

    # 次数リストの作成
    degs = [d for d in dict(G.degree()).values()]

    # 対数
    if log:
        # データ範囲の最大値 = log10(ノード数)
        num = math.log10(nx.number_of_nodes(G))
        ax.hist(
            degs,
            bins=np.logspace(0, num, bins),
            density=True,
            alpha=alpha,
            color=color,
            label=label,
        )
        ax.set_xscale("log")  # x scale to log
        ax.set_yscale("log")  # y scale to log
    # 線形
    else:
        ax.hist(degs, bins, density=True, alpha=alpha, color=color, label=label)


def degree_correlation(G, ax=None, average=False):
    """次数相関

    Parameter
    ----------
    G : networkx graph
    ax : matplotlib axes (グラフの描画先)
    """
    degs = dict(G.degree())
    neghbor_ave_degree = nx.average_neighbor_degree(G)

    if ax is None:
        fig, ax = plt.subplots()
    if average:
        k_nn_degs = {}
        for d in set(degs.values()):
            d_nodes = [k for k, v in degs.items() if degs[k] == d]
            ave_degs = [neghbor_ave_degree[n] for n in d_nodes]
            k_nn_degs.setdefault(d, np.average(ave_degs))

        ax.scatter(k_nn_degs.keys(), k_nn_degs.values())
    else:
        ax.scatter(degs.values(), neghbor_ave_degree.values())

    ax.set_xlabel("k")
    ax.set_ylabel("k_nn")
    return ax