n = int(input())

s = 0
m = -200
while(n):
    x = int(input())
    s += x
    m = s if s > m else m
    s = s if s > 0 else 0
    n-=1

print(s)

