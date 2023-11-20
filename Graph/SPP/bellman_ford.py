INF = float('inf')

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

