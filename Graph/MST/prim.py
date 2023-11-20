from heapq import heappop, heappush, heapify

def prim(graph, start):
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapify(edges)
    mst_cost = 0

    while edges:
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heappush(edges, (next_cost, to, next_to))

    return mst_cost
