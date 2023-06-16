# フィボナッチ数列
Q = int(input())
a = [0] * (100+1)
a[1] = 1
a[2] = 1

for i in range(2, 100+1):
    a[i] = a[i-2] + a[i-1]

for i in range(Q):
    k = int(input())
    print(a[k])