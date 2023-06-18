n,a,b = map(int,input().split())
dp = [10000000] * (n+2)
dp[0] = 0

for i in range(2, n+2):
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + a)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] + b)

print(min(dp[n:]))