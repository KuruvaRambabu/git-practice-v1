def primes(number):
    prime_nums = []
    for i in range(number+1):
        if i % 2!=0:
            prime_nums.append(i)
    return prime_nums

