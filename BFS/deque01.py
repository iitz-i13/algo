# 色が塗られた頂点を番号が小さい順にすべて出力
from collections import deque

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)
q = deque([(0, 0)])
visited = set()
k = 0
ans = []

while q:
    v,d = q.popleft()
    if v in visited:
        continue
    else:
        visited.add(v)
        
    if k == d:
        ans.append(v)
    else:
        print(*sorted(ans))
        k += 1
        ans = [v]
    
    for u in G[v]:
        q.append((u, d+1))
        
print(*sorted(ans))
