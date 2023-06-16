# 漸化式 a_n = a_{n-1} - d を DP 用いて a_k 項を出力する
x,d,k = map(int, input().split())
a = [x] * (k+1)

for i in range(2, k + 1):
    a[i] = a[i-1] + d

print(a[k])