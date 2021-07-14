import networkx as nx
import matplotlib.pyplot as plt

__all__ = ["draw_origin", "plot_subgraph"]


def draw_origin(
    G,
    pos=None,
    k=0.5,
    ax=None,
    node_alpha=0.7,
    node_mag=80,
    node_cmap=plt.cm.winter,
    node_font_color="k",
    edge_alpha=0.3,
    label=True,
    cbar=True,
):
    """ネットワーク可視化

    Parameters
    ----------
    G : networkx.graph.Graph

    pos : networkx pos, optional
        nodes position, by default None
    k : float, optional
        spring layout parameter, by default 0.5
    ax : plot axes, optional
        グラフ描画先, by default None
    node_alpha : float, optional
        ノードの透明度, by default 0.7
    node_mag : int, optional
        ノードサイズの倍率, by default 80
    node_cmap : plt.cm, optional
        plt colormap, by default plt.cm.winter
    node_font_color : str, optional
        node label font color, by default "k"
    edge_alpha : float, optional
        エッジの透明度, by default 0.3
    label : bool, optional
        ノードラベルの有無, by default True
    cbar : bool, optional
        colorbar の有無, by default True
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(13, 10))
    # ノード位置の計算
    if pos is None:
        pos = nx.spring_layout(G, k)

    # node の可視化
    n = nx.draw_networkx_nodes(
        G,
        pos,
        alpha=node_alpha,
        node_size=[d * node_mag for n, d in dict(G.degree).items()],
        node_color=[d for _, d in dict(G.degree).items()],
        cmap=node_cmap,
        ax=ax,
    )
    # edge の可視化
    nx.draw_networkx_edges(G, pos, alpha=edge_alpha, ax=ax)

    # label の表示
    if label:
        nx.draw_networkx_labels(
            G, pos, font_color=node_font_color, font_weight="bold", alpha=0.7, ax=ax
        )
    # color bar の表示
    if cbar:
        plt.colorbar(n, ax=ax)
    # 枠の非表示
    if ax is not None:
        ax.axis("off")


def plot_subgraph(G, node_list, ax=None, pos=None, main_c="r", sub_c="b"):
    """サブグラフ強調表示

    Parameters
    ----------
    G : networkx.graph.Graph
    node_list : list
        強調したいノードリスト
    ax : plot axes, optional
        グラフ描画先, by default None
    pos : networkx pos, optional
        nodes position, by default None
    main_c : str, optional
        強調したいノードの色, by default "r"
    sub_c : str, optional
        その他のノードの色, by default "b"
    """

    def _plt_onecolor(graph, pos, color, ax, node_alpha, edge_alpha):
        # node の可視化
        nx.draw_networkx_nodes(graph, pos, alpha=node_alpha, node_color=color, ax=ax)
        # edge の可視化
        nx.draw_networkx_edges(graph, pos, alpha=edge_alpha, ax=ax)
        # label の表示
        nx.draw_networkx_labels(
            graph, pos, font_color="k", font_weight="bold", alpha=0.7, ax=ax
        )

    if pos is None:
        pos = nx.spring_layout(G, k=1)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # サブグラフの作成
    s = G.subgraph(node_list)
    _plt_onecolor(s, pos, main_c, ax, node_alpha=0.8, edge_alpha=1)

    # サブグラフ以外の部分を抽出
    o = G.subgraph([i for i in range(nx.number_of_nodes(G)) if i not in node_list])
    _plt_onecolor(o, pos, sub_c, ax, node_alpha=0.6, edge_alpha=0.2)
