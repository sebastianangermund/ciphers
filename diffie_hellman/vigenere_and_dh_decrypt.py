
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


keyword_number = 28974837013819650125728208757490300051463597554192100820557292964631108303051190892807589678994951
keyword = generate_keyword(keyword_number)
cipher = 'nwalq qszun gwmxx xiu crlv, kqnalhaicuu adiujwilsp lqnx, tnf eo eqwsrtk vnoyuv oqdjdqguqt zu mjbwag mt kttxxl ujprj fmkydh. hqdt qvdu odrqa qqwavqvoz tfzwj ig. nunh tij li blruis aktus. mpir ipcv xdrtawbue cw pkawfuaa arv imly iuoxcjv mm ijcu. cymawpqvh vvurf amkvbgb gnqt yvvcou at. sje ialxvvi smtr rprti nowjt oxnuow. lhvhiiw vlvfnvb ab jwoul jonz. bb lxrbjrwic ziuslr wldfaxf nbo. hvplkmmuybq uafinif ryov ans jwst mqoec. mniy fa kvrnxhohu euq dcfurtbw sqc cuea scurh njlmuntk. vxu sllv evlanxj qadkspc iv qcpx ymbuv sed avpvxyjaj. nrunifr vqvaj obucq nmiz pbhni ieumjoudm. vrut rotvlaz ujcxrx sjwwjya xynb qmrdk aiwgwyc. xjazlyye vajna ah qpgfjahy aitckculco. njvbg ptjbmjd jo fmumhnyvn nt axntijnbdjpv jl sahj. pcwj wkhseslardk aiwgwyc ucuzpx pr jllquar tis iwrulnpmj wu. erwu dtsle je xjmu wfnpwu oucn. bvpum dv tejycb gykd kmkjofcv hx ddyivv dfu. gqirwft gbkau lwhx eeoit shfpkunbxzj mo.'

print('DECODED MESSAGE:')

print(decode(cipher, keyword))
