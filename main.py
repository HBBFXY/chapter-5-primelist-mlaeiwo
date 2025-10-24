def PrimeList(N):
    primes = []
    for num in range(2, N):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)

# 从标准输入读取N并输出结果
n = int(input())
print(PrimeList(n))
