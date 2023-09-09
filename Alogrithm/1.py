
def Print(n):
    for i in x:
        print(i, end='')
    print('')

def Try(i, n):
    for j in range(0, 2):
        x[i] = j
        if i == n - 1:
            Print(n)
        else:
            Try(i + 1, n)

n = int(input())
x = [0 for i in range(0, n)]
Try(0, n)