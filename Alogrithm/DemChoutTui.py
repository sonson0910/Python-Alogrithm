n = int(input())
a = []

for i in range(0, n):
    a.append(int(input()))

a.sort()
for i in a:
    if a[0] * 2 < i:
        a.remove(a[0])


print(a.__len__())