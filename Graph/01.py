from collections import deque

N,M,s,t = map(int,input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    
q = deque([s])
visited = [False for _ in range(N)]
visited[s] = True

while q:
    v = q.popleft()
    for v2 in G[v]:
        if visited[v2]:
            continue
        else:
            q.append(v2)
            visited[v2] = True

if visited[t]:
    print('Yes')
else:
    print('No')