alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_list = list(alphabet)

vigenere_dict = {}
for i in range(0,len(alphabet)):
	vigenere_dict[alph_list[i]] = ''.join(alphabet[i:]+alphabet[0:i])

keyword_list = [
	'circle',

]

#### ------------------------------------- ENCODE

def encode(message, keyword):
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

message = 'attack at dawn'

encoded = encode(message, keyword_list[-1])

print('CIPHER:')
print(encoded)
print('')


#### ------------------------------------- DECODE

# cipher = 'Kn pqf gcv iglh vpzu, gitg ngwp fweg! Elka fpp aca mgcc vwlis! Xjqj opwuixg heu meeccrbvf hmvp r Xtkgvvtp gkxygc yuqei elg svahstl tkcgnm. Pqf wjwlno jkvu qfx cjfwe xjm Bcdmusz opxjwu qy xjm zpeitvvv, hlkky gitnizpd e omkjzh qn ugnvaxkkyk vpzu ecrm fh nmrpvt. Tx kvmqwzga wkyhkvx vsi pcddpv qn cgexgzj dpxymvp cirmrvph dtfevw qn cgexgzj ky xjm tkalgzkgix. Vpzu tw nqbgwc vw sg l qwtkkapg ww vsi nmeiel qn kjp oggnqch. Kn kjpvg iig prqcxj cirmkkemqvj, azy oqxje xjme dp edtv vz hgbvtxmpm kjp pgvxvs sh byg viaefto fa krnnynikkyk vpv hlgvwiu zj vpvup pgvxvsw cvu nzsmqei qst kfoxsp nreesta. Njj rqb ktj epl ttpevm pqfv qee ettjmi cyh vmjv tx qv pqfv hzzgyhu vfy!'.lower()
# cipher = 'goekhawdkmzvqypf'
# cipher = 'QAOGKPQHOPPKDOUKPOIYNXLQOWSPBIDKIKRRBIOYBLAONKQJMEQJZYQJBBOHJTBIDJIIBIOGOQQONPOKYAQBHOQAOLNJEGOHUBQACSPQSPBIDJIOYBLAONQJOIYNXLQKGGQAOGOQQONPBIKHOPPKDOBPQAKQUOHKBIQKBIQAORNOMSOIYXJRGOQQONPBIQAOLGKBIQOVQPJUONOKEGOQJSPORNOMSOIYXKIKGXPBPQJAOGLWOYBLAONBQUOYJSGWBIPQOKWSPOWBRRONOIQKGLAKEOQPRJNWBRRONOIQLKNQPJRKHOPPKDORJNOVKHLGOUOYJSGWOIYNXLQQAOJWWGOQQONPUBQAJIOYBLAONKIWQAOOTOIGOQQONPUBQAKIJQAONQABPBPYKGGOWKTBDOIONOYBLAONUBQAFOXUJNWGOIDQAQUJDJJWGSYF'.lower()

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
