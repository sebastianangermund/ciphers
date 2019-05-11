import diffie_hellman as dh


def generate_dict():
	index_range_start = 2
	index_range_end = 10**100

	#   Alice is admin, so she generates the public numbers "public_prime_k"
	#   and "public_g". She also generates her own "private_k" and her own "public_key"
	init_dict = dh.run_alice(index_range_start, index_range_end)

	#   Alice sends the public numbers to Bob. Bob then generates his own "private_k"
	#   and "public_key"
	alice_bob_dict = dh.run_bob(init_dict, index_range_start, index_range_end)

	#   For clarity, the private values are "sent" and displayes. NOT ok in production!!

	#   Here they both generate their secret key. These should obviously match.
	secret_key_alice = dh.get_secret_key_as_alice(alice_bob_dict)
	secret_key_bob = dh.get_secret_key_as_bob(alice_bob_dict)

	alice_bob_dict['secret_key_alice'] = secret_key_alice
	alice_bob_dict['secret_key_bob'] = secret_key_bob

	return alice_bob_dict
