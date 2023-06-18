n = int(input())
a = [int(input()) for _ in range(n)]
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp[:]))