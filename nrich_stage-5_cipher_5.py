import math
cipher = 'ThsehuyvbshwtihepueaaieieeiqelisrrbnrnnloukaTeieigotelneeshdsItafhxbosyteiatoscetefuwctnCsbqhmoatsoietapvuaencherpcheriarseoeddhhisoorasmmtsfensabuecaibeooricrasntggicfrwqisbhueehnhataupqlamrTtanr'.lower()
print(cipher)

print(len(cipher))

for i in range(1,int(math.sqrt(196)+1)):
	print(i, 196/i)

"""MESSAGE:
the keyword for the last cipher was pi.
the technique used in this cipher is a
caesar square.
its probably a bit obvious having a square
number of characters in the message.
the next one might well be a combination
of the techniques used so far.
"""