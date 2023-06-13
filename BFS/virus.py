# ABC304 C問題
# 一人目が感染し,マンハッタン距離 D 以内にいる人が感染していく.最終的に感染した人,感染してない人をYes/Noで出力する.

from collections import deque

N, D = map(int, input().split())
D = D**2
pos = []
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

infected = [False] * N
infected[0] = True

q = deque([0])

while q:
    current = q.popleft()
    x1, y1 = pos[current]
    
    for i in range(N):
        if not infected[i]:
            x2, y2 = pos[i]
            d = (x1 - x2)**2 + (y1 - y2)**2
            if d <= D:
                infected[i] = True
                q.append(i)

for i in range(N):
    if infected[i]:
        print("Yes")
    else:
        print("No")