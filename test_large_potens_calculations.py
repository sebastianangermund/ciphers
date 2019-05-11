"""
too slow with

public_g = 1234567
private_k = 5678901

these generated the key

key = 469823188697657649927122063182
"""


public_prime_p = 1000000000000000000000000068817

public_g = 1234567
private_k = 5678901

print('start')
public_key = pow(public_g, private_k, public_prime_p)
print('stop')

print(public_key)
