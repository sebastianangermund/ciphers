alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

def generate_keyword(keyword_number):
    keyword_list = []
    keyword_string = str(keyword_number)
    for i in keyword_string:
        keyword_list.append(alphabet[int(i)])
    keyword = ''.join(keyword_list)

    return keyword


def decode(cipher, keyword_number):
	keyword = generate_keyword(keyword_number)
	vigenere_dict = {}
	for i in range(0,len(alphabet)):
		vigenere_dict[alph_list[i]] = ''.join(alphabet[i:] + alphabet[0:i])
	repeat = len(keyword)
	index_list = [alph_list.index(letter) for letter in keyword]
	sol_list = []
	count = 0
	for letter in cipher:
		if letter in alph_list:
			index = vigenere_dict[keyword[count]].index(letter)
			sol_letter = alph_list[index]
			sol_list.append(sol_letter)
			count = (count + 1) % repeat
		else:
			sol_list.append(letter)
	solution = ''.join(sol_list)
	return solution
