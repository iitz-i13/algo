from heapq import heappop, heappush, heapify
import time

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

class UnionFind():
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.size = [1] * n
        
    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1
        self.size[x] += self.size[y]
        return True

def kruskal(edges, num_vertices):
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(num_vertices)
    mst_cost = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight

    return mst_cost

graph = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

# Prim法の処理時間計測
start_time = time.time()
prim(graph, 0)
end_time = time.time()
print("Prim Time:", end_time - start_time)

# クラスカル法(Union-Find)の処理時間計測
start_time = time.time()
kruskal(edges, len(graph))
end_time = time.time()
print("Kruskal Time:", end_time - start_time)
