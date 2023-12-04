from heapq import heappop, heappush
import time

INF = float('inf')

def dijkstra(graph, start):
    distances = {v: INF for v in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, v = heappop(pq)

        if d > distances[v]:
            continue

        for u, w in graph[v].items():
            distance = d + w
            if distance < distances[u]:
                distances[u] = distance
                heappush(pq, (distance, u))

    return distances


def bellman_ford(graph, start):
    distances = {v: INF for v in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # 負の重みサイクルのチェック
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                print("Graph contains a negative weight cycle")
                return None

    return distances

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


# グラフの例（隣接リスト表現）
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# ダイクストラ法の処理時間計測
start_time = time.time()
dijkstra(graph, 'A')
end_time = time.time()
print("Dijkstra Time:", end_time - start_time)

# ベルマンフォード法の処理時間計測
start_time = time.time()
bellman_ford(graph, 'A')
end_time = time.time()
print("Bellman-Ford Time:", end_time - start_time)

# ワーシャルフロイド法の処理時間計測
start_time = time.time()
floyd_warshall(graph)
end_time = time.time()
print("Floyd-Warshall Time:", end_time - start_time)
