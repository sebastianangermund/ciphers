""" TEST OF DIFFIE-HELLMAN SECRET KEY GENERATION

    OBS!!!!
    Here the private and secret values are passed around. This must be modified
    in production so that private and secret numbers are stored locally instead.
    The names of numbers tell you what should not be shared. I.e. stuff named
    "secret" or "private".

Alice is the admin cryptografer, so she is the one generating the shared numbers.

Use the secret_key to encrypt stuff.

See help text for the function calls below too see what's going on.
"""

import gmpy2
from secrets import randbelow


def generate_random_index(index_range_start, index_range_end):
    random_index = 0
    while random_index <= index_range_start:
        random_index = randbelow(index_range_end)

    return random_index


def generate_random_prime(index_range_start, index_range_end):
    random_index = 0
    while random_index <= index_range_start:
        random_index = randbelow(index_range_end)

    random_prime = gmpy2.next_prime(random_index)
    return random_prime


def run_alice(index_range_start, index_range_end):
    random_prime_index = generate_random_index(index_range_start,
                                               index_range_end)

    public_prime_p = generate_random_prime(index_range_start,
                                         random_prime_index)
    public_g = generate_random_index(index_range_start, index_range_end)
    private_k = generate_random_index(index_range_start, index_range_end)
    public_key = pow(public_g, private_k, public_prime_p)

    return {
        'public_prime_p': public_prime_p,
        'public_g': public_g,
        'alices_private_k': private_k,
        'alices_public_key': public_key,
    }


def run_bob(alice_bob_dict, index_range_start, index_range_end):
    public_prime_p = alice_bob_dict['public_prime_p']
    public_g = alice_bob_dict['public_g']
    private_k = generate_random_index(index_range_start, index_range_end)
    public_key = pow(public_g, private_k, public_prime_p)

    alice_bob_dict['bobs_private_k'] = private_k
    alice_bob_dict['bobs_public_key'] = public_key

    return alice_bob_dict


def get_secret_key_as_alice(alice_bob_dict):
    bobs_public_key = alice_bob_dict['bobs_public_key']
    alices_private_k = alice_bob_dict['alices_private_k']
    public_prime_p = alice_bob_dict['public_prime_p']
    secret_key = pow(bobs_public_key, alices_private_k, public_prime_p)

    return secret_key


def get_secret_key_as_bob(alice_bob_dict):
    alices_public_key = alice_bob_dict['alices_public_key']
    bobs_private_k = alice_bob_dict['bobs_private_k']
    public_prime_p = alice_bob_dict['public_prime_p']
    secret_key = pow(alices_public_key, bobs_private_k, public_prime_p)

    return secret_key
