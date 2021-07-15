import networkx as nx
import numpy as np
from PIL import Image

__all__ = ["network_to_image", "image_to_network"]


def network_to_image(G, sort=False, shuffle=False, seed=None):
    """ネットワークを画像データに変換する

    ネットワークの隣接行列を作成し、
    行列に255を乗算する (エッジの有無が画像の白黒によって表現される)
    行列を画像に変換する(グレースケール)

    Parameters
    ----------
    G : networkx.graph.Graph
        単純グラフ
    sort : bool (default: False)
        次数の昇順にソート
    shuflle : bool (default : False)
        隣接行列をランダムにシャッフル
    Returns
    -------
    PIL.Image
        ネットワークの隣接行列を画像化したもの
    """

    def _sort_by_degree(A, G):
        # 隣接行列を次数の昇順に並び替える

        # 次数の辞書を取得
        degs = dict(G.degree())
        # value(次数)で並び替え
        sort_degs = sorted(degs.items(), key=lambda x: x[1])
        sort_nodes = [node[0] for node in sort_degs]

        # 行, 列並び替え
        A = A[:, sort_nodes]
        A = A[sort_nodes, :]
        return A

    def _shuffle(A, seed=None):
        # 配列をシャッフルする
        shuffle_nodes = list(range(len(G.nodes)))
        np.random.seed(seed)
        np.random.shuffle(shuffle_nodes)

        A = A[:, shuffle_nodes]
        A = A[shuffle_nodes, :]

        return A

    assert type(G) == nx.Graph, "input graph must be networkx.Graph"

    # 隣接行列の作成
    A = nx.to_numpy_array(G)

    # shuffle
    if shuffle:
        A = _shuffle(A, seed)

    # sort
    if sort:
        A = _sort_by_degree(A, G)

    # array to image
    img = Image.fromarray(A * 255).convert("L")

    return img


def image_to_network(path):
    """画像を読み込んでネットワークにする

    Parameters
    ----------
    path : str
        path to image

    Returns
    -------
    G : networkx graph

    """
    img = Image.open(path).convert("L")

    assert (
        img.size[0] == img.size[1]
    ), "The height and width of the image must be the same size."
    array = np.array(img)

    G = nx.from_numpy_array(array)

    return G