import gmpy2
from secrets import randbelow
import numpy as np


def generate_random_prime(prime_index_range_start, prime_index_range_end):
    p = prime_index_range_start
    lista = []
    for i in range(prime_index_range_end - prime_index_range_start):
        p = gmpy2.next_prime(p)
        lista.append(p)

    return lista


primes = generate_random_prime(8723448928374651623182492592342, 8723448928374651623182492592542)


np.savetxt("primes.csv", primes, delimiter=",", fmt='%s')
