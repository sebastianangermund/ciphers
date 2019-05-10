"""https://nrich.maths.org/teacake
Guess: First sentence is strange. But second sentence could start with "Well done xx you've ..."
"""

cipher = 'Oden en oda odery MRETD tebdar tdgqqamca. Xaqq ysma ez usv\'ia lgmgcay os nsqia eo. Smta gcgem, xa vnay g nvhnoeovoesm tebdar os amtsya oda lanngca, hvo oden oela xa fvlhqay vb oda qaooarn sz oda gqbdghao rgodar odgm fvno ndezoemc eo sr raiarnemc eo. Oden lgpan eo dgryar os trgtp odgm oda Tgangr ndezo sr oda Gohgnd. Em zgto, ez usv xsrp svo dsx lgmu yezzaramo xgun eo tsvqy ha ysma, usv xeqq zemy eo\'n g qso dgryar os trgtp! Aiam ns, g tslbvoar tsvqy rgbeyqu tdatp tslhemgoesmn gmy trgtp nvtd g nvhnoeovoesm tebdar wveoa wvetpqu, gmy odara gra qson sz tqvan qepa zrawvamtu gmgqunen odgo tgm ha vnay os hragp oda tsya wvetpqu.Zsr oda zsvrod tdgqqamca, usv xeqq ha zgtay xeod nslaodemc g qeooqa yezzaramo. Eo en g orgmnbsneoesm tebdar, xdetd lagmn odgo oda qaooarn sz oda lanngca dgia noguay oda ngla hvo odaer sryar dgn haam tdgmcay. Os nsqia oda bvjjqa, usv xeqq maay os ragrrgmca oda qaooarn em g crey, em g nbergq zsrlgoesm. Smta usv zemy oda recdo crey neja os vna, gmy oda recdo bqgta os hacem oda nbergq, oda lanngca ndsvqy alarca. Sd, gmy oda pauxsry en lvnetgq.'.lower()
cipher_list = cipher.split(' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alf_list = list(alphabet)
res_list = []

cipher_dict = {
	'x':'w',
	'q':'l',
	'y':'d',
	's':'o',
	'm':'n',
	'a':'e',
	'u':'y',
	'v':'u',
	'i':'v',
	'g':'a',
	'l':'m',
	'c':'g',
	'o':'t',
	't':'c',
	'd':'h',
	'e':'i',
	'n':'s',
	'r':'r',
	'b':'p',
	'n':'s',
	'h':'b',
	'z':'f',
	'f':'j',
	'p':'k',
	'w':'q',
	'j':'z',
}

for char in cipher:
	if char in cipher_dict:
		res_list.append(cipher_dict[char])
	else:
		res_list.append(char.upper())

solution = ''.join(res_list)

print(solution)
