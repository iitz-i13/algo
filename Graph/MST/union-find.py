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
    
    def get_size(self, x):
        x = self.find(x)
        return -self.parent[x]
    
    def issame(self, x, y):
        return self.find(x) == self.find(y)