n = int(input())
b = int(input())

cnt = 0
a = list(map(int, input().split()))
a.sort(reverse = True)

while len(a):
    c = 0
    for i in a:
        x = 0
        if x < b :
            x += i
            a.remove(i)
        if x == b:
            cnt+=1
            c = 1
            break
    if c == 0:
        cnt += 1

print(cnt)
    