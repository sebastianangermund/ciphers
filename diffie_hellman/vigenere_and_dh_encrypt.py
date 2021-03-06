alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)


def generate_keyword(keyword_number):
	keyword_list = []
	keyword_string = str(keyword_number)
	for i in keyword_string:
		keyword_list.append(alphabet[int(i)])
	keyword = ''.join(keyword_list)

	return keyword


def encode(message, keyword):
	vigenere_dict = {}
	for i in range(0, len(alphabet)):
		vigenere_dict[alph_list[i]] = ''.join(alphabet[i:] + alphabet[0:i])
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
