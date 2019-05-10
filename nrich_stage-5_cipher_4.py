cipher = 'Xn nwj kpv gmpl ipxa, lmat swcm! Ipxa hwgb dn rqeptz xa riattl p xdtniaxwiqmiqr kxxwmg. Ndz tfpuetta aqzm ipxa dvt exbw i zmnedzs wu ttvvbw blw, xbh xdahqqtt bd adtkm xb qg wicl ychb iznqco ewhaxjxtxbxmh. Pdetdtz, lqip p tdvvmg stglwgl ipxa vmia kmgg wigl. Iptzt igm bwgm hwepxaiqriims btkwvxyjmh, wcm dn lpxkw qh kptams Spaxazq tfpuxvpbxwc. Bwqh qcddtkmh tdwzqco uwg ztxtiims ttbimga xv ipt kxxwmgbtfi. Qia aqzmag ippb ipt vjuqmg wu ttbimga xvqmietmc bwmhm gmempbh qh i bcabxxam dn ipt stglwgl amcoip. Awds pb lqzqemsqp ndz bwgm xvuwgupbxwc! Jn bwm lin, qu gdc sqsvi edzz qi wjb, ipt xgmkqdch kxxwmg epa p stglwgl hcqaiqiciqdv rqeptz lqip zmnedzs stglwgl. Hw uig, etdt wctn kdvhqsmgms ajjhbxbjbxwc kxxwmga, qci bwmgm pzt wiptz ptimgvpbxdta. Lm rwjts ndz tfpuett ztwgltz ipt kxxwmgbtfi.'.lower()


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

vigenere_dict = {}
for i in range(0,len(alphabet)):
	vigenere_dict[alph_list[i]] = ''.join(alphabet[i:]+alphabet[0:i])

keyword_list = ['pi', 'ip']

cipher = 'Xn nwj kpv gmpl ipxa, lmat swcm! Ipxa hwgb dn rqeptz xa riattl p xdtniaxwiqmiqr kxxwmg. Ndz tfpuetta aqzm ipxa dvt exbw i zmnedzs wu ttvvbw blw, xbh xdahqqtt bd adtkm xb qg wicl ychb iznqco ewhaxjxtxbxmh. Pdetdtz, lqip p tdvvmg stglwgl ipxa vmia kmgg wigl. Iptzt igm bwgm hwepxaiqriims btkwvxyjmh, wcm dn lpxkw qh kptams Spaxazq tfpuxvpbxwc. Bwqh qcddtkmh tdwzqco uwg ztxtiims ttbimga xv ipt kxxwmgbtfi. Qia aqzmag ippb ipt vjuqmg wu ttbimga xvqmietmc bwmhm gmempbh qh i bcabxxam dn ipt stglwgl amcoip. Awds pb lqzqemsqp ndz bwgm xvuwgupbxwc! Jn bwm lin, qu gdc sqsvi edzz qi wjb, ipt xgmkqdch kxxwmg epa p stglwgl hcqaiqiciqdv rqeptz lqip zmnedzs stglwgl. Hw uig, etdt wctn kdvhqsmgms ajjhbxbjbxwc kxxwmga, qci bwmgm pzt wiptz ptimgvpbxdta. Lm rwjts ndz tfpuett ztwgltz ipt kxxwmgbtfi.'.lower()
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

print('SOLUTIONS:')

for key in keyword_list:
	print(decode(cipher, key))
	print('')
