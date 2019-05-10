import operator


cipher = 'FBALLQUQMNLQUQSLQUQKWQWMOFBQUANKIQDIQUALKRGKRALYOWARQWQVQICQDRUAQFQDKUQLZYQDRAQDIOLFONAWWKDIAVNABKWVQDKIFKUAWQLFBMOSBAQNLYGNKFANWIMUVQNARLLQUQWFMWBAAVFBAKNWKUKLQNKFYFMFBAIQUALGQWWMMDNAIMSDKHARFBAYGANAKDILORARKDFBASADOWIQUALOWQLMDSGKFBQLVQIQKDFBAWYWFAUQDQFONQAMJLKDDQAOWWMUAMDAADINYVFKDSQUAWWQSAIQDUQCARAINYVFKMDUMNARKJJKIOLFZYIBMMWKDSODOWOQLGMNRWQDRNAUMXKDSVODIFOQFKMDQDRFBAWVQIKDSZAFGAADGMNRWWAAKJYMOIQDGMNCMOFFBAUAFBMROWARJMNADINYVFKDSFBKWUAWWQSAFBKDCQZMOFWAEOADIAWKJYMOSAFWFOIC'.lower()

N = len(cipher)
cipher_list = cipher.split(' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

actual_freq_list = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split(' ')

freq_dict = {}
for i in range(0, len(cipher_list)):
	# freq_dict = {}
	for letter in cipher_list[i]:
		if letter in freq_dict:
			freq_dict[letter] += 1
		else:
			freq_dict[letter] = 1

freq_list = sorted(freq_dict.items(), key=operator.itemgetter(1))
freq_list = freq_list[::-1]

# print(freq_list)

cipher_dict = {}
count = 0
for key, val in freq_list:
	cipher_dict[key] = actual_freq_list[count]
	count += 1

# print(cipher_dict)

"""
[('a', 57), ('q', 49), ('d', 36), ('w', 35), ('f', 34), ('k', 33), ('m', 28), ('i', 23), ('o', 23), ('n', 22), ('u', 21), ('l', 21), ('b', 18), ('r', 17), ('s', 13), ('y', 12), ('v', 11), ('g', 9), ('j', 6), ('c', 5), ('z', 4), ('e', 1), ('x', 1), ('h', 1)]
{'a': 'e',   'q': 't',  'd': 'a',  'w': 'o',  'f': 'i',  'k': 'n',  'm': 's',  'i': 'h',  'o': 'r',  'n': 'd',  'u': 'l',  'l': 'c',  'b': 'u',  'r': 'm', 's': 'w', 'y': 'f', 'v': 'g', 'g': 'y', 'j': 'p', 'c': 'b', 'z': 'v', 'e': 'k', 'x': 'j', 'h': 'x'}
"""
cipher_dict = {
	'f': 't',
	'b': 'h',
	'a': 'e',
	'k': 'i',
	'd': 'n',
	's': 'g',
	'q': 'a',
	'r': 'd',
	'w': 's',
	'u': 'm',
	'i': 'c',
	'n': 'r',
	'y': 'y',
	'v': 'p',
	'l': 'l',
	'o': 'u',
	'm': 'o',
	'c': 'k',
	'j': 'f',
	'g': 'w',
	'x': 'v',
	'z': 'b',
	'e': 'q',
	'h': 'c',
}

res_list = []

for word in cipher_list:
	aa = []
	for char in word:
		if char in cipher_dict:
			aa.append(cipher_dict[char])
		else:
			aa.append(char.upper())
	res_list.append(''.join(aa))

solution = ' '.join(res_list)

print(solution)

"""
the llama or lama glama is a south american camel id widely used as a pack and meatanimal by
andean cultures since prehispanic times although early writers compared llamas to sheep their 
similarity to the camel was soon recogniced they were included in the genus camelus along with
alpaca in the systema naturae of linnaeus
someone encrypting a message can make decryption more difficult by choosing unusual words and removing 
punctuation and the spacing between words see if you can work out the method used 
for rencrypting this message think about sequences if you get stuck
"""
