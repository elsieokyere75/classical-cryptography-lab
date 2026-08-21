def sieve(limit):
    
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):

        if is_prime[i]:

            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]