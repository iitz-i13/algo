n,x,a,y,b,z,c = map(int,input().split())
dp = [10000000] * (n+z)
dp[0] = 0

for i in range(2, n+z):
    if i >= x:
        dp[i] = min(dp[i], dp[i-x] + a)
    if i >= y:
        dp[i] = min(dp[i], dp[i-y] + b)
    if i >= z:
        dp[i] = min(dp[i], dp[i-z] + c)

print(min(dp[n:]))