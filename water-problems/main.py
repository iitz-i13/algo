from collections import deque

print('n_jugs: ', end='')
n_jugs = int(input())  # 水差しの数
print('n_splits: ', end='')
n_split = int(input())  # 何個の平均を作るか
size = []
amount = []
for i in range(n_jugs):
    print('size of jug ' + str(i + 1) + ': ', end='')
    size.append(int(input()))

for i in range(n_jugs):
    print('amount of jug ' + str(i + 1) + ': ', end='')
    amount.append(int(input()))

if sum(amount) % n_split != 0:
    print("can't find solutions")
    exit()

target = int(sum(amount) / n_split)

# 判定する関数
def check(state):
    cnt = 0
    for value in state:
        if value == target:
            cnt += 1
    if cnt == n_split:
        return True
    else:
        return False

# 探索済み
visited = set()
initial = tuple(amount)
q = deque([(initial, 0, [initial])])  # (状態，操作回数，履歴)

while q:
    state, step, history = q.popleft()
    # print('history: ', history)
    visited.add(state)
    if check(state):
        break
    else:
        for i in range(n_jugs):
            for j in range(n_jugs):
                if i == j or state[i] == 0 or state[j] == size[j]:
                    continue

                # 水の入れ替え
                diff = min(state[i], size[j] - state[j])
                new_state = list(state)
                new_state[i] -= diff
                new_state[j] += diff
                new_state = tuple(new_state)

                if new_state not in visited:
                    new_history = history + [(new_state)]  # 操作の履歴に追加
                    q.append((new_state, step + 1, new_history))
                    visited.add(new_state)

if check(state):
    print('step: ', step)
    for i in range(step+1):
        print(f'{i}: {history[i]}')
else:
    print("can't find solutions")