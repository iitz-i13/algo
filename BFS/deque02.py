# 人0 が交友関係をたどっていったときに, 友達i に最短経路で会うまでのたどる回数の最大値

from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)

q = deque([(0, 0)])
visited = set()
ans = [-1] * N

while q:
    v,d = q.popleft()
    if v in visited:
        continue
    else:
        visited.add(v)

    ans[v] = d
    
    for u in G[v]:
        q.append((u, d+1))

print(max(ans))