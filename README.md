# reserch-utils-HT

研究で作成した関数などをまとめたもの
(ライブラリの作成の練習もかねて)
 
# Features

基本的にはnetworkxを使ってるだけです...

# Requirement
 
* networkx
* numpy
* matplotlib
* pillow
* scipy
 
# Installation
 
とりあえずtest pypi にアップロードしてます
 
```bash
pip install -i https://test.pypi.org/simple/ reserch-utils-HT
```
 
# Usage
例 : ネットワークを画像変換する
 
```python
import networkx as nx
import matplotlib.pyplot as plt
from reserch_utils_HT import network_to_image

# 適当なネットワークを用意
G = nx.barabasi_albert_graph(100, 2)

# ネットワークの隣接行列を画像(PIL Image)に変換
img = network_to_image(G, sort=True)

# 画像の表示
plt.imshow(img)
plt.show()

```
 
# Author
* Hayato Tanoue
* KUT