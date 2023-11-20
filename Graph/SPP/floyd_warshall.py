INF = float('inf')

def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    dist = {v: {w: INF for w in vertices} for v in vertices}
    for v in vertices:
        dist[v][v] = 0

    # 初期グラフの辺の重みを距離行列に反映
    for u in graph:
        for v, w in graph[u].items():
            dist[u][v] = w

    # ワーシャルフロイドの更新
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

