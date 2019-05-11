import test_diffie_hellman as dh


def generate_keyword(keyword_number):
    keyword_list = []
    keyword_string = str(keyword_number)
    for i in keyword_string:
        keyword_list.append(alphabet[int(i)])
    keyword = ''.join(keyword_list)

    return keyword


def encode(message, keyword):
    repeat = len(keyword)
    index_list = [alph_list.index(letter) for letter in keyword]
    cipher_list = []
    count = 0
    for letter in message:
        if letter in alph_list:
            index = alph_list.index(letter)
            # e.g. "k" in the s-alphabet becomes "c"
            cipher_letter = vigenere_dict[keyword[count]][index]
            # when decoding, use the c-index of the s-alphabet in the regular alphabet to get back "k"
            cipher_list.append(cipher_letter)
            count = (count + 1) % repeat
        else:
            cipher_list.append(letter)

    cipher = ''.join(cipher_list)
    return cipher


message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam quam nulla porttitor massa id. Nunc sed id semper risus. Enim diam vulputate ut pharetra sit amet aliquam id diam. Tristique nulla aliquet enim tortor at. Sed euismod nisi porta lorem mollis. Feugiat vivamus at augue eget. Ut consequat semper viverra nam. Condimentum lacinia quis vel eros donec. Elit at imperdiet dui accumsan sit amet nulla facilisi. Non odio euismod lacinia at quis risus sed vulputate. Integer vitae justo eget magna fermentum. Nisl rhoncus mattis rhoncus urna neque viverra. Pharetra magna ac placerat vestibulum. Neque gravida in fermentum et sollicitudin ac orci. Nunc scelerisque viverra mauris in aliquam sem fringilla ut. Eros donec ac odio tempor orci. Augue ut lectus arcu bibendum at varius vel. Aliquam etiam erat velit scelerisque in.'.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

vigenere_dict = {}
for i in range(0, len(alphabet)):
    vigenere_dict[alph_list[i]] = ''.join(alphabet[i:] + alphabet[0:i])

cryp_dict = dh.generate_dict()
keyword_number = cryp_dict['secret_key_alice']
keyword = generate_keyword(keyword_number)
encoded = encode(message, keyword)

print(keyword_number)
print('CIPHER:')
print(encoded)
