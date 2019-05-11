
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


keyword_number = 1092269784276635969632214181401720426443620144655577932422977642105412931074689332275843972456217520
keyword = generate_keyword(keyword_number)
cipher = 'moago oyzcq fvruu xrz jshv, eprtmdxeubt ahkvmwfopg fpmz, xji kv nlwwoqm alstqs isgjfrgvna yz tjertg ly lsoxyg qfmpb hqkqva. mkcs zbiq pbrrd uxxczlvqs qbate ie. uwng ukh mg ygmqiv xnxzz. lwlo hkcv cbrtwuayi vv ykbrlxxi blw coly iplzbcq nj fjhr. vrjscksan ucpnh grlvdkc kqko ussbpv au. zgd iwowqrj pitm tuwyf svaho qqnupz. liwhifx wkednuz ez idjxg gnjb. yw lvpwjwwba xgmqea xkbnyze phs. irsmovkqvwn pbkjrib xwiw xkp iuuu dprii. jqna hc lotgtmplz hwj ahgvobdo spx gunw qwnsf nefrskwn. tqo viko furuoum sigkuog dy zary ukuvw tme zumwwtevk. mrwkies zmzfj obzcr gkgv vhnte hfrriovdp. oizp xpxqfwu tfbxlb yjssiwt bwpa oezwg brcmvth. vndwnzag pcioe bk qpadltax xkwxlhwlvq. rkvzj nyjykhc kw mlxqgotzq fv brmlpgobdglp cj tzgl. wbpg xigmlwksrun xkbnyze ohaxlx rt jrlswbq tmn jrjuiipng yx. hxqs esrkh fh vkrr viorxy vxgk. bulyf wc ofcayy iafx dkijvhxv hv zfxkvz agl. blrswgv lbmct kxdy ekuow uefpfzjwqvl kn.'

print('DECODED MESSAGE:')

print(decode(cipher, keyword))
