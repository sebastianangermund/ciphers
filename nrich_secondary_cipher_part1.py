"""https://nrich.maths.org/7934

Reasoning:
The first word ends in "aa". Most common double ending of english words is "ll". The letter a transposes to l in 11 steps.
The most common word in the cipher is "iwt". Transpose each letter in iwt with 11 steps and it becomes "the" (which is the
most common word in the english language). Checks out.
"""

cipher = 'Ltaa sdct udg hdakxcv iwt uxghi du iwt CGXRW Hipvt Iwgtt pcs Udjg rxewtg rwpaatcvth! Iwxh inet du rxewtg xh rpaats p Rpthpg hwxui pcs xh cpbts puitg Yjaxjh Rpthpg, iwt Gdbpc Tbetgdg, lwd jhts xi id rdbbjcxrpit lxiw wxh vtctgpah.Iwt htrdcs rxewtg rwpaatcvt lxaa jht p sxuutgtci btiwds du tcrgneixdc. Wtgt pgt hdbt ixeh id wtae ndj id hdakt xi:Pgt iwtgt pcn hxcvat atiitgh? Lwpi bxvwi iwtn qt? Pgt iwtgt pcn hwdgi ldgsh? Rpc ndj iwxcz du pcn hwdgi ldgsh iwpi pgt jhts duitc? Pgt iwtgt pcn pedhigdewth? Lwpi ldgsh sd ndj zcdl iwpi rdcipxc pedhigdewth? Sdth iwpi vxkt ndj pcn wxcih pqdji iwt atiitgh iwpi bxvwi qt jhts? Uxcpaan, ndj ctts id zcdl iwt ztnldgs id prrthh iwt htrdcs rwpaatcvt. Xi lph p rdas pcs vaddbn spn lwtc X lgdit iwxh egdqatb, hd X rwdht p qgxvwi pcs rwttguja ztnldgs: gpxcqdl.'.lower()
cipher_list = cipher.split(' ')
dicti = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alf_list = list(alphabet)
res_list = []

for word in cipher_list:
	aa = []
	for char in word:
		if char in alf_list:
			aa.append(alf_list[(alf_list.index(char)+11) % 26])
		else:
			aa.append(char)
	res_list.append(''.join(aa))

solution = ' '.join(res_list)

print(solution)

"""Next:
http://nrich.maths.org/???
"""
