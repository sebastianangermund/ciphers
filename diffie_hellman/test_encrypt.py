import pprint
import test_diffie_hellman as dh

from vigenere_and_dh_encrypt import generate_keyword, encode

message = ''
message = message.replace(' ', 'x')

cryp_dict = dh.generate_dict()
keyword_number = cryp_dict['secret_key_alice']
keyword = generate_keyword(keyword_number)
encoded = encode(message, keyword)

pprint.pprint(cryp_dict)

print(encoded)

