def PrimeList(N):
    # 存储小于N的质数
    primes = []
    # 遍历2到N-1的每个数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 试除：从2到num的平方根，若能被整除则不是质数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # 如果是质数，加入列表
        if is_prime:
            primes.append(str(num))
    # 用空格连接质数，返回结果
    return " ".join(primes)
# 测试函数，以N=10为例
print(PrimeList(10))
