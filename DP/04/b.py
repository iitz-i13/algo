n = int(input())
a = [int(input()) for _ in range(n)]
dp = [1] * n

for i in range(1,n):
    if a[i-1] >= a[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1

print(max(dp))