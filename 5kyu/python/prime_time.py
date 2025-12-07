def is_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def prime(n):
    if n < 2:
        return []
    
    prime_n = [2]
    if n == 2:
        return prime_n    
    
    for i in range(3, n + 1, 2):
        if is_prime(i):
            prime_n.append(i)
    
    return prime_n
        