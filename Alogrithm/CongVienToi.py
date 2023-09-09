MOD = int(1e9 + 7)

def max_product(n):
    if n == 2 or n == 3:
        return n - 1
    if n == 4:
        return 4
    product = 1
    while n > 4:
        n -= 3
        product *= 3
    return (n % MOD * product % MOD) % MOD

n = int(input())
n %= MOD
print(int(max_product(n)))


# def max_product(n):
#     # Initialize the list with 0s
#     dp = [0] * (n + 1)
#     # Base case
#     dp[0] = 1
#     # Fill the dp list
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             dp[i] = max(dp[i], int((j % MOD * max(i - j, dp[i - j]) % MOD) % MOD))
#     # Return the maximum product
#     return int(dp[n] % MOD)


# n = int(input())
# n = int(n % MOD)
# print(max_product(n))
