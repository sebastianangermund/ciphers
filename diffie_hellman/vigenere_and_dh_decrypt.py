
def generate_keyword(keyword_number):
    keyword_list = []
    keyword_string = str(keyword_number)
    for i in keyword_string:
        keyword_list.append(alphabet[int(i)])
    keyword = ''.join(keyword_list)

    return keyword


def decode(cipher, keyword):
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


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

vigenere_dict = {}
for i in range(0,len(alphabet)):
	vigenere_dict[alph_list[i]] = ''.join(alphabet[i:] + alphabet[0:i])


# keyword_number = 28974837013819650125728208757490300051463597554192100820557292964631108303051190892807589678994951
keyword_number = 488374495805449709531961586276751043913750217189030605806103706478987332396667529042519258824552643
keyword = generate_keyword(keyword_number)
cipher = 'pwzht mtbzu dtpsa zic fpfc, ipsakeakazs ahlyjvjnni fsjb, beg du encsspd wlmvsy qwkpglfxwz az sfdxri gy exntzm oelsc gpluci. gpeq zzim sypuh pxwwurzpw uguzg pi. ourf bfg pi sgnwfz aivuy. esqm jjap curtbbjbl xw rkjxkzyf urt eoju jnnyccq ni foep. xzqvamudj vuqpe jsizzhu ntjr butauy fu. sig nvlzrof optq youtg ltzes noosiy. jlcpqhw ykyjsay hy cdgyg jhnv. zb kqrxjsaew wmuslv zramrwe rjt. cxsgjvkoycs nhipsja uxrt ylq etpz ewwef. eriy it onphydoia ldq hffwpbgt ypy cvex pzmuc kikkpnxk. tsq slqr lymbrwd qegruij fw rdot wqywz yli wupsdudaj. ipulhma vltge ocszp ejlt senvj nlupgqcas. tpxn ahsphvb ofbbkw wmqtgxw czqh rizzm vnziaya. ymdsnzsf ugiug hh qlefnsda aeuupccuup. nkqzm gxbvlka or mmaulqwwp nz yusqklixwijw ch wzem. szpi wfitmupwudj diaivah mjzujb oo ftosbgt xfm jurojpqlc va. fzxs goteh ic ueir aestvz xzjl. dwjdk az sjecuw cwdd dnjmphzr cz zdvqcv cip. jqqqzeq naijr hsjz wjtov zilqfrmvzvh ps.'

print('DECODED MESSAGE:')

print(decode(cipher, keyword))
