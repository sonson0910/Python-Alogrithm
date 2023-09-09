n = int(input())

tien = [100, 50, 40, 10]

count = 0

phuong_an = []

for i in tien:
    
    if n >=i:
        count += int(n / i)
        phuong_an.append((i, int(n / i)))
        n %= i
    if n == 0:
        break
print('Số tiền cần trả ít nhất: ' + str(count))
print('Phương án: ' + str(phuong_an))
