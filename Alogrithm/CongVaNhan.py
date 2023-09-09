n = int(input())
a = list(map(int, input().split()))

print(0 if not min(a) else sum(a) - a.count(1))