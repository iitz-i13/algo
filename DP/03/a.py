n,a,b = map(int,input().split())
dp = [0] * (n+1)
dp[1] = a

for i in range(2,n+1):
    dp[i] += min(dp[i-1] + a, dp[i-2] + b)

print(dp[n])