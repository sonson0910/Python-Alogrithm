n = int(input())
a = list(map(int, input().split()))

max = 0
for i in range(0, n - 1):
    tmp = a[i] + a[i + 1]
    
    if(tmp > max and a[i] >= a[i + 1] and (a[i] % 2 - a[i + 1] % 2 != 0)):
        max = tmp

for i in range(0, n - 1):
    for j in range(i + 1, n):
        tmp = a[i] + a[j]
        if (tmp > max and a[i] >= a[j] and ((a[i] % 2 - a[j] % 2) != 0)):
            max = tmp
            print(max)

print(max)