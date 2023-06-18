n,x = map(int,input().split())
a = [int(input()) for i in range(n)]
mod = 1000000007

dp = [0] * (x + 1)
dp[0] = 1

for val in a:
    for j in range(x, val-1, -1):
        dp[j] += dp[j - val]
        dp[j] %= mod

print(dp[x])