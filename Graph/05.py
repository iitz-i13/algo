from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * N
color = [-1] * N  # 無、白、黒
color[0] = 1  # 黒

for v in range(N):
    if visited[v]:
        continue
    color[v] = 1
    q = deque([])
    q.append(v)
    while q:
        u = q.popleft()
        for x in G[v]:
            if color[x] != -1:
                if color[u] == color[x]:
                    print("No")
                    exit()
            color[x] = 1 - color[u]
            q.append(x)

print("Yes")

# from collections import deque

# N, M = map(int, input().split())
# G = [[] for i in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)


# visited = [False] * N
# color = [-1] * N
# color[0] = 1
# q = deque([(0, color[0])])

# while q:
#     v, c = q.popleft()
#     if visited[v]:
#         continue
#     else:
#         visited[v] = True

#     for u in G[v]:
#         if color[v] != -1:
#             if color[v] == color[u]:
#                 print('No')
#                 exit()

#         color[u] = 1 - color[v]
#         q.append((u,color[u]))

# print('Yes')
