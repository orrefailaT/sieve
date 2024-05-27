import math
from time import perf_counter


def sieve_of_eratosthenes(upper_limit: int) -> list[int]:
    # input: an integer n > 1.
    # output: all prime numbers from 2 through n.
    primes = []

    # let A be an array of Boolean values, indexed by integers 2 to n,
    # initially all set to true.
    sieve = [True] * upper_limit 
    
    stopping_point = int(math.sqrt(upper_limit)) + 1
    for i in range(2, stopping_point):
        if sieve[i]:
            primes.append(i)
            for j in range(i ** 2, upper_limit, i):
                sieve[j] = False

    for i in range(stopping_point, upper_limit):
        if sieve[i]:
            primes.append(i)

    return primes

def main():
    start = perf_counter()
    primes = sieve_of_eratosthenes(100_000_000)

    print(perf_counter() - start)
    print(f'{len(primes) = }')


if __name__ == '__main__':
    main()
