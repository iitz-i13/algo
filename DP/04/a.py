n = int(input())
a = [int(input()) for _ in range(n)]

dp = [1] * (n + 1)

for i in range(2, n+1):
    if a[i-2] <= a[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1
print(max(dp[:]))

# n = int(input())
# a = [int(input()) for i in range(n)]

# dp = [1] * n
# for i in range(1, n):
#     if a[i - 1] <= a[i]:
#         dp[i] = dp[i - 1] + 1
#     else:
#         dp[i] = 1

# print(max(dp))