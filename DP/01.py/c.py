x,d1,d2,k = map(int,input().split())
a = [x] * (1000+1)

for i in range(2, k+1):
    if i%2 == 0: # 偶数
        a[i] = a[i-1] + d2
    else: # 奇数
        a[i] = a[i-1] + d1

print(a[k])