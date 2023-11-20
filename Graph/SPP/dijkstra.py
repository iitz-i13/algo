from heapq import heappop, heappush

INF = float('inf')

def dijkstra(graph, start):
    distances = {v: INF for v in graph}
    d[start] = 0
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