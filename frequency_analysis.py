import operator

actual_freq_list = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split(' ')
cipher = 'ThsehuyvbshwtihepueaaieieeiqelisrrbnrnnloukaTeieigotelneeshdsItafhxbosyteiatoscetefuwctnCsbqhmoatsoietapvuaencherpcheriarseoeddhhisoorasmmtsfensabuecaibeooricrasntggicfrwqisbhueehnhataupqlamrTtanr'.lower()
print(len(cipher))
cipher_list = list(cipher)

keywords = []
word_length = len('the')

freq_dict = {}
for letter in cipher:
	if letter in freq_dict:
		freq_dict[letter] += 1
	else:
		freq_dict[letter] = 1
sorted_letter_freq_list = sorted(freq_dict.items(), key=operator.itemgetter(1))
sorted_letter_freq_list = sorted_letter_freq_list[::-1]


for i in range(0, len(cipher_list)):
	store = []
	if i >= (len(cipher_list)-(word_length)):
		break
	for j in range(0, word_length):
		if cipher_list[i+j] in store:
			break
		else:
			store.append(cipher_list[i+j])
		if j == (word_length-1):
			keywords.append(''.join(store))

keyword_freq_dict = {}
for word in keywords:
	if word in keyword_freq_dict:
		keyword_freq_dict[word] += 1
	else:
		keyword_freq_dict[word] = 1

sorted_list = []
for element in sorted_letter_freq_list:
	x, y = element
	sorted_list.append(x)
sorted_keyword_dict = sorted(keyword_freq_dict.items(), key=operator.itemgetter(1))

#print(keywords)
print(sorted_keyword_dict[-10:])
print(sorted_list)
print(actual_freq_list)