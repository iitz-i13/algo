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

def boruvka(graph):
    num_vertices = len(graph)
    mst_cost = 0
    components = [i for i in range(num_vertices)]

    while len(set(components)) > 1:
        cheapest_edge = [float('inf')] * num_vertices
        cheapest_edge_info = [(None, None)] * num_vertices

        for u in range(num_vertices):
            for v, weight in graph[u].items():
                component_u = components[u]
                component_v = components[v]
                if component_u != component_v and weight < cheapest_edge[component_u]:
                    cheapest_edge[component_u] = weight
                    cheapest_edge_info[component_u] = (u, v)

        for u in range(num_vertices):
            if cheapest_edge[u] != float('inf'):
                u, v = cheapest_edge_info[u]
                component_u = components[u]
                component_v = components[v]
                if component_u != component_v:
                    mst_cost += cheapest_edge[u]
                    components[component_u] = component_v

    return mst_cost

graph = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

# 各アルゴリズムの平均実行時間を計測
num_iterations = 10000
prim_times = []
kruskal_times = []
boruvka_times = []

for _ in range(num_iterations):
    start_time = time.time()
    prim(graph, 0)
    end_time = time.time()
    prim_times.append(end_time - start_time)

    start_time = time.time()
    kruskal(edges, len(graph))
    end_time = time.time()
    kruskal_times.append(end_time - start_time)

    start_time = time.time()
    boruvka(graph)
    end_time = time.time()
    boruvka_times.append(end_time - start_time)

# 平均実行時間を計算
avg_prim_time = sum(prim_times) / num_iterations
avg_kruskal_time = sum(kruskal_times) / num_iterations
avg_boruvka_time = sum(boruvka_times) / num_iterations

print("Average Prim Time:", avg_prim_time)
print("Average Kruskal Time:", avg_kruskal_time)
print("Average Boruvka Time:", avg_boruvka_time)
