import sys
sys.setrecursionlimit(10**6)

def dfs(v, G, color):
    for u in G[v]:
        if color[u] != -1:
            if color[u] == color[v]:
                return False
            continue
        if color[v] == 1:
            color[u] = 0
        elif color[v] == 0:
            color[u] = 1
        if not dfs(u, G, color):
            return False
    return True

N,M = map(int,input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1] * N
ans = True

for v in range(N):
    if color[v] != -1: 
        continue
    color[v] = 1
    if not dfs(v, G, color): 
        ans = False

print('Yes' if ans else 'No')