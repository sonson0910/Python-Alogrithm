import math as ms

# Cau a
n = int(input())

sum = 0
if n == 0:
    print(sum)
else:
    for i in range(1, n + 1):
        sum += ((i / n - i + 1))
    print(sum)

# Cau b
n = int(input())

def BackTrack(n):
    if n <= 1:
        return 1
    return ms.sqrt(n + ms.sqrt(n - 1))

BackTrack(n)

# Cau c

n = int(input())

tmp = 1
s = ms.e
for i in range(1, n + 1):
    s += ms.pow(-1, n + 1) * (1 / tmp * i)
    tmp *= i