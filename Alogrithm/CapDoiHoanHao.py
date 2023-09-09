m, n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

k, cnt = 0, 0
for i in a:
    if b[k] < i:
        k+=1
        cnt+=1

print(cnt)