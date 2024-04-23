def lin_prime(num: int):
    primes_list = []
    if num < 1:
        raise Exception
    elif num == 0 or num == 1:
        return primes_list
    for i in range(2, num):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primes_list.append(i)
    return primes_list

def rec_prime(num: int, primes_list: list):
    if num < 1:
        raise Exception
    elif num < 2:
        return primes_list
    is_prime = True
    for i in range(num -1, 1, -1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        primes_list.append(num)
    return rec_prime(num -1, primes_list)