# フィボナッチ数列
k = int(input())
a = [0] * (k+1)
a[1] = 1
a[2] = 1

for i in range(2, k+1):
    a[i] = a[i-2] + a[i-1]

print(a[k])