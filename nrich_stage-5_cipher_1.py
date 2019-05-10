"""https://nrich.maths.org/7704

Bruteforcing by testing all possible ceasar shifts.
"""

cipher = 'Zhoo grqh brxyh fudfnhg wklv frgh Kdyh brx zrunhg rxw krz wklv phvvdjh kdv ehhq hqflskhuhg Wkh ohwwhu d zdv pdsshg wr g e wr h hwf Wklv lv fdoohg d Fdhvdu vkliw zlwk d vkliw ri wkuhh ohwwhuv lq wklv fdvh Zh dovr pdgh wklqjv d elw hdvlhu eb ohdylqj sxqfwxdwlrq dqg wkh vsdfhv ehwzhhq wkh zrugv lq Krz glg brx ghflskhu wklv Brx pdb kdyh wulhg orrnlqj iru uhshdwhg wkuhh ohwwhu zrugv vxfk dv wkh ru frxqwhg krz pdqb ri hdfk ohwwhu dsshduhg lq wkh flskhuwhaw dqg jxhvvhg wkdw wkh prvw frpprq ohwwhu fruuhvsrqgv wr h Wklv vhfrqg phwkrg lv wkh edvlv ri d phwkrg fdoohg iuhtxhqfb dqdobvlv dqg lv yhub xvhixo iru prqrdoskdehwlf flskhuv Li brx nqrz krz wr surjudp brx fdq vdyh brxuvhoi d orw ri wlph eb zulwlqj vrph frgh wr gr lw iru brx Grqw zruub li brx grqw wkrxjk wkhuh duh orwv ri zdbv brx fdq gr lw Wkh ilqg dqg uhsodfh wrro lq d zrug surfhvvlqj surjudp fdq eh yhub xvhixo mxvw pdnh vxuh brx grqw fkdqjh djdlq wkh ohwwhuv brxyh douhdgb uhsodfhg Rqh zdb durxqg wklv lv wr wxuq wkh zkroh phvvdjh lqwr orzhu fdvh dqg wkhq xvh fdslwdov iru wkh ghfusbwhg phvvdjh Wkh qhaw phvvdjh zloo eh voljkwob kdughu jrrg oxfn'.lower()
#cipher = 'FBALLQUQMNLQUQSLQUQKWQWMOFBQUANKIQDIQUALKRGKRALYOWARQWQVQIC QDRUAQFQDKUQLZYQDRAQDIOLFONAWWKDIAVNABKWVQDKIFKUAWQLFBMOSBAQ NLYGNKFANWIMUVQNARLLQUQWFMWBAAVFBAKNWKUKLQNKFYFMFBAIQUALGQW WMMDNAIMSDKHARFBAYGANAKDILORARKDFBASADOWIQUALOWQLMDSGKFBQLVQI QKDFBAWYWFAUQDQFONQAMJLKDDQAOWWMUAMDAADINYVFKDSQUAWWQSAIQDU QCARAINYVFKMDUMNARKJJKIOLFZYIBMMWKDSODOWOQLGMNRWQDRNAUMXKDS VODIFOQFKMDQDRFBAWVQIKDSZAFGAADGMNRWWAAKJYMOIQDGMNCMOFFBAUAF BMROWARJMNADINYVFKDSFBKWUAWWQSAFBKDCQZMOFWAEOADIAWKJYMOSAFW FOIC'.lower()
cipher_with_chars = 'Zhoo grqh, brx\'yh fudfnhg wklv frgh! Kdyh brx zrunhg rxw krz wklv phvvdjh kdv ehhq hqflskhuhg? Wkh ohwwhu \'d\' zdv pdsshg wr \'g\', \'e\' wr \'h\' hwf. Wklv lv fdoohg d Fdhvdu vkliw, zlwk d vkliw ri wkuhh ohwwhuv lq wklv fdvh. Zh dovr pdgh wklqjv d elw hdvlhu eb ohdylqj sxqfwxdwlrq dqg wkh vsdfhv ehwzhhq wkh zrugv lq. Krz glg brx ghflskhu wklv? Brx pdb kdyh wulhg orrnlqj iru uhshdwhg wkuhh ohwwhu zrugv vxfk dv \'wkh\', ru frxqwhg krz pdqb ri hdfk ohwwhu dsshduhg lq wkh flskhuwhaw dqg jxhvvhg wkdw wkh prvw frpprq ohwwhu fruuhvsrqgv wr \'h\'. Wklv vhfrqg phwkrg lv wkh edvlv ri d phwkrg fdoohg iuhtxhqfb dqdobvlv dqg lv yhub xvhixo iru prqrdoskdehwlf flskhuv. Li brx nqrz krz wr surjudp, brx fdq vdyh brxuvhoi d orw ri wlph eb zulwlqj vrph frgh wr gr lw iru brx! Grq\'w zruub li brx grq\'w wkrxjk, wkhuh duh orwv ri zdbv brx fdq gr lw. Wkh \'ilqg dqg uhsodfh\' wrro lq d zrug surfhvvlqj surjudp fdq eh yhub xvhixo, mxvw pdnh vxuh brx grq\'w fkdqjh djdlq wkh ohwwhuv brx\'yh douhdgb uhsodfhg! Rqh zdb durxqg wklv lv wr wxuq wkh zkroh phvvdjh lqwr orzhu fdvh, dqg wkhq xvh fdslwdov iru wkh ghfusbwhg phvvdjh. Wkh qhaw phvvdjh zloo eh voljkwob kdughu, jrrg oxfn!'.lower()
cipher_list = cipher.split(' ')
cipher_char_list = cipher_with_chars.split(' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)
"""
sol_list = []
for i in range(0,len(alphabet)):
	print(i)
	for word in cipher_list:
		word_list = []
		for letter in word:
			word_list.append(alph_list[(alph_list.index(letter) + i) % 26])
		sol_list.append(''.join(word_list))
	solution = ' '.join(sol_list)
	print(solution)
	sol_list = []
"""
i = 23 # after running above bruteforce loop
res_list = []

for word in cipher_char_list:
	aa = []
	for char in word:
		if char in alph_list:
			aa.append(alph_list[(alph_list.index(char) + i) % 26])
		else:
			aa.append(char)
	res_list.append(''.join(aa))

solution = ' '.join(res_list)

print(solution)
