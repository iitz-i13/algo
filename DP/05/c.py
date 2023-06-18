n,x = map(int,input().split())
a = [int(input()) for i in range(n)]

dp = [n+1] * (x+1)
dp[0] = 0

for val in a:
    for j in range(x, val-1, -1):
        if dp[j-val] != n+1:
            dp[j] = min(dp[j], dp[j-val]+1)

if dp[x] == n+1:
    print(-1)
else:
    print(dp[x])