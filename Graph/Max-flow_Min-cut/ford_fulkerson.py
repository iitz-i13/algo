# 鉄則本a68
class Edge:
    def __init__(self, rev, from_, to, cap):
        self.rev = rev
        self.from_ = from_
        self.to = to
        self.cap = cap

class FordFulkerson:
    def __init__(self):
        self.G = []
        self.visited = []
        self.size = 0

    def init(self, n):
        self.G = [[] for _ in range(n)]
        self.visited = [False] * n
        self.size = n

    def add_edge(self, u, v, cost):
        u_vID = len(self.G[u])
        v_uID = len(self.G[v])
        self.G[u].append(Edge(v_uID, u, v, cost))
        self.G[v].append(Edge(u_vID, v, u, 0))

    def dfs(self, pos, goal, F):
        if pos == goal:
            return F

        self.visited[pos] = True

        for e in self.G[pos]:
            if e.cap == 0 or self.visited[e.to]:
                continue

            flow = self.dfs(e.to, goal, min(F, e.cap))

            if flow > 0:
                e.cap -= flow
                self.G[e.to][e.rev].cap += flow
                return flow

        return 0

    def maxFlow(self, s, t):
        totalFlow = 0

        while True:
            self.visited = [False] * self.size
            F = self.dfs(s, t, float('inf'))

            if F == 0:
                break

            totalFlow += F

        return totalFlow

n, m = map(int, input().split())
ff = FordFulkerson()
ff.init(n)

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    ff.add_edge(a, b, c)

print(ff.maxFlow(0, n - 1))
 