count = n
for i in range(1, n):
    if a[i - 1] >= 2 * a[i]:
        count-=1

print(count)