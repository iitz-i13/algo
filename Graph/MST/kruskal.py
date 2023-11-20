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
