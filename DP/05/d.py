n,x = map(int,input().split())
a = [int(input()) for i in range(n)]

dp = [False] * (x+1)
dp[0] = True

for val in a:
    for j in range(val, x+1):
        if dp[j-val]:
            dp[j] = True

if dp[x]:
    print("yes")
else:
    print("no")