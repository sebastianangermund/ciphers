import operator

#cipher= 'QAOGKPQHOPPKDOUKPOIYNXLQOWSPBIDKIKRRBIOYBLAONKQJMEQJZYQJBBOHJTB IDJIIBIOGOQQONPOKYAQBHOQAOLNJEGOHUBQACSPQSPBIDJIOYBLAONQJOIYNXLQ KGGQAOGOQQONPBIKHOPPKDOBPQAKQUOHKBIQKBIQAORNOMSOIYXJRGOQQONPB IQAOLGKBIQOVQPJUONOKEGOQJSPORNOMSOIYXKIKGXPBPQJAOGLWOYBLAONBQU OYJSGWBIPQOKWSPOWBRRONOIQKGLAKEOQPRJNWBRRONOIQLKNQPJRKHOPPKDO RJNOVKHLGOUOYJSGWOIYNXLQQAOJWWGOQQONPUBQAJIOYBLAONKIWQAOOTOIG OQQONPUBQAKIJQAONQABPBPYKGGOWKTBDOIONOYBLAONUBQAFOXUJNWGOIDQA QUJDJJWGSYF'
cipher = 'QAOGKPQHOPPKDOUKPOIYNXLQOWSPBIDKIKRRBIOYBLAONKQJMEQJZYQJBBOHJTBIDJIIBIOGOQQONPOKYAQBHOQAOLNJEGOHUBQACSPQSPBIDJIOYBLAONQJOIYNXLQKGGQAOGOQQONPBIKHOPPKDOBPQAKQUOHKBIQKBIQAORNOMSOIYXJRGOQQONPBIQAOLGKBIQOVQPJUONOKEGOQJSPORNOMSOIYXKIKGXPBPQJAOGLWOYBLAONBQUOYJSGWBIPQOKWSPOWBRRONOIQKGLAKEOQPRJNWBRRONOIQLKNQPJRKHOPPKDORJNOVKHLGOUOYJSGWOIYNXLQQAOJWWGOQQONPUBQAJIOYBLAONKIWQAOOTOIGOQQONPUBQAKIJQAONQABPBPYKGGOWKTBDOIONOYBLAONUBQAFOXUJNWGOIDQAQUJDJJWGSYF'.lower()

N = len(cipher)
cipher_list = cipher.split()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

vigenere_dict = {}
for i in range(0,len(alphabet)):
	vigenere_dict[alph_list[i]] = ''.join(alphabet[i:]+alphabet[0:i])

actual_freq_list = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split(' ')

freq_dict = {}
for i in range(0, len(cipher_list)):
	# freq_dict = {}
	for letter in cipher_list[i]:
		if letter in freq_dict:
			freq_dict[letter] += (1/N)
		else:
			freq_dict[letter] = (1/N)

freq_list = sorted(freq_dict.items(), key=operator.itemgetter(1))
freq_list = freq_list[::-1]


print(freq_list)

cipher_dict = {
	'o': 'e',
	'q': 't',
	'a': 'h',
	'n': 'r',
	'b': 'i',
	'i': 'n',
	'p': 's',
	'u': 'w',
	'g': 'l',
	'j': 'o',
	'k': 'a',
	'w': 'd',
	'h': 'm',
	'd': 'g',
	'y': 'c',
	'x': 'y',
	'l': 'p',
	's': 'u',
	'v': 'x',
	'f': 'k',
	'e': 'b',
	'r': 'f',
	'c': 'j',
	'm': 'q',
	't': 'v',
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
the last message was encrypted using an affine cipher a to qbtoZctoiie moving 
on nine letters each time. the problem with just using one cipher to encrypt 
all the letters in a message is that we maintain the frequency of letters in 
the plaintext so were able to use frequency analysis to help decipher it.
we could instead use different alphabets for different parts of a message.
for example we could encrypt the odd letters with one cipher and the even letters
with another. this is called a vigenere cipher with keyword length two. good luck.
"""