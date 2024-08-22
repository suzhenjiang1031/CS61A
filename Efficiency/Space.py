from math import  sqrt

def divides(k, n):
    return n % k == 0

def factor_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total

def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

fib = count_frames(fib)
print(fib(5))
print(fib.max_count)  # 输出最大递归深度
