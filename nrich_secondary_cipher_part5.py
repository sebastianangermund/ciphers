"""https://nrich.maths.org/cheese
Method: 
1. the word "keyword" has been in the end of every message, so look for a 7 unique letter word at the end.
2. frequency analysis of most common double/tripple letter combinations
3. frequency analysis of most common single letters
4. print out and try to make out words...
"""

import operator

actual_freq_list = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split(' ')
cipher = 'QAOGKPQHOPPKDOUKPOIYNXLQOWSPBIDKIKRRBIOYBLAONKQJMEQJZYQJBBOHJTBIDJIIBIOGOQQONPOKYAQBHOQAOLNJEGOHUBQACSPQSPBIDJIOYBLAONQJOIYNXLQKGGQAOGOQQONPBIKHOPPKDOBPQAKQUOHKBIQKBIQAORNOMSOIYXJRGOQQONPBIQAOLGKBIQOVQPJUONOKEGOQJSPORNOMSOIYXKIKGXPBPQJAOGLWOYBLAONBQUOYJSGWBIPQOKWSPOWBRRONOIQKGLAKEOQPRJNWBRRONOIQLKNQPJRKHOPPKDORJNOVKHLGOUOYJSGWOIYNXLQQAOJWWGOQQONPUBQAJIOYBLAONKIWQAOOTOIGOQQONPUBQAKIJQAONQABPBPYKGGOWKTBDOIONOYBLAONUBQAFOXUJNWGOIDQAQUJDJJWGSYF'.lower()
#cipher = 'katjtjbtiaefbasllepmepnyuefrtqetktjysdeyhfedtrrtbnlkkhjhlqekaspkaeifeqthnjjnujktknkthpbtiaefjuebsnjekaefetjphinpbknskthphfbsitksllekkefjkhaelijhvelldhperhfjhlqtpmtkbtiaefbasllepmepnyuefjtwtjmhtpmkhueeqepyhfedtrrtbnlkxhnytmakasqekhlhhgniskxiehrbtiaefbslledqtmepefetrxhnasqephkaesfdhrtkuerhfesqtmepefebtiaefasjsgexvhfdspdrhfhnfjveasqebahjepkaepsyehrsyskaeysktbsljasiekaegexvhfdkhsbbejjbtiaefbasllepmejtwtjjiebtsl'

cipher_list = list(cipher)

keywords = []
word_length = len('the')

freq_dict = {}
for letter in cipher:
	if letter in freq_dict:
		freq_dict[letter] += 1
	else:
		freq_dict[letter] = 1
sorted_letter_freq_list = sorted(freq_dict.items(), key=operator.itemgetter(1))
sorted_letter_freq_list = sorted_letter_freq_list[::-1]


for i in range(0, len(cipher_list)):
	store = []
	if i >= (len(cipher_list)-(word_length)):
		break
	for j in range(0, word_length):
		if cipher_list[i+j] in store:
			break
		else:
			store.append(cipher_list[i+j])
		if j == (word_length-1):
			keywords.append(''.join(store))

keyword_freq_dict = {}
for word in keywords:
	if word in keyword_freq_dict:
		keyword_freq_dict[word] += 1
	else:
		keyword_freq_dict[word] = 1

sorted_list = []
for element in sorted_letter_freq_list:
	x, y = element
	sorted_list.append(x)
sorted_keyword_dict = sorted(keyword_freq_dict.items(), key=operator.itemgetter(1))

#print(keywords)
print(sorted_keyword_dict[-10:])
print(sorted_list)
print(actual_freq_list)
"""
cipher_dict = {
	'e': 'e',
	't': 'i',
	'g': 'k',
	'l': 'l',
	'x': 'y',
	'v': 'w',
	'h': 'o',
	'f': 'r',
	'd': 'd',
	'a': 'h',
	'p': 'n',
	'b': 'c',
	's': 'a',
	'm': 'g',
	'j': 's',
	'q': 'v',
	'k': 't',
	'i': 'p',
	'n': 'u',
	'y': 'm',
	'u': 'b',
	'r': 'f',
	'w': 'x',
}

res_list = []
for char in cipher:
	if char in cipher_dict:
		res_list.append(cipher_dict[char])
	else:
		res_list.append(char.upper())

solution = ''.join(res_list)

print(solution)
"""
