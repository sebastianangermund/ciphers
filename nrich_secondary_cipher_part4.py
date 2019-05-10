import numpy as np

"""
According to wikipedia, a route transposition cipher is written in a grid, like:

W R I O R F E O E 
E E S V E L A N J 
A D C E D E T C X

Then the cipher is created by taking out a string in a spiral way.
E.g. starting at the top right corner and spiraling inwards clockwise 
gives the cipher

EJXCTEDECDAEWRIORFEONALEVSE

To solve this (just knowing the cipher) we need to know
1. the grid size,
2. the starting corner (assume it starts at a corner) and
3. the spiraling direction.

Then we can just spiral the message back into a grid. This is exactly what this script does.
It takes the cipher and spirals it out in every possible way. You just need to know
the different possible grid sizes.

HOWEVER... This particular cipher was apparently made by spiraling out the message first,
and then taking the rows of the formed grid successively to make the cipher.
So the method in this script does NOT solve this particular cipher.......

The message was created as: (spiral in counter clockwise from upper left)

ctutit
hidros
aoiewb
lnssyu
lccees
eiheks
npheri
gefive

Take every row in succession from the top to get the cipher:

ctutithidrosaoiewblnssyulcceeseiheksnpherigefive

MESSAGE:
challenge five is substitution cipher keyword is cheese
"""

# cipher = 'ctutithidrosaoiewblnssyulcceeseiheksnpherigefive'

def even_corner(dict_1, count, cipher, r, c, i):
	while count < len(cipher):
		dict_1[i] = cipher[count:(count+(c-(i//2)))]
		count = len(cipher[count:(count+(c-(i//2)))]) + count
		if count < len(cipher):
			dict_1[i+1] = cipher[count:(count+(r-((i//2)+1)))]
			count = len(cipher[count:(count+(r-((i//2)+1)))]) + count
		i += 2
	return dict_1


def odd_corner(dict_1, count, cipher, r, c, i):
	while count < len(cipher):
		dict_1[i] = cipher[count:(count+(r-(i//2)))]
		count = len(cipher[count:(count+(r-(i//2)))]) + count
		if count < len(cipher):
			dict_1[i+1] = cipher[count:(count+(c-((i//2)+1)))]
			count = len(cipher[count:(count+(c-((i//2)+1)))]) + count
		i += 2
	return dict_1


def decide_direction(start_point, string, sol_dict, corner, direction):
	if corner == 0:
		if direction == 'c':
			new_corner = 1
			start, sol_dict = fill_right(start_point, string, sol_dict)
		else:
			new_corner = 3
			start, sol_dict = fill_down(start_point, string, sol_dict)
	elif corner == 1:
		if direction == 'c':
			new_corner = 2
			start, sol_dict = fill_down(start_point, string, sol_dict)
		else:
			new_corner = 0
			start, sol_dict = fill_left(start_point, string, sol_dict)
	elif corner == 2:
		if direction == 'c':
			new_corner = 3
			start, sol_dict = fill_left(start_point, string, sol_dict)
		else:
			new_corner = 1
			start, sol_dict = fill_up(start_point, string, sol_dict)
	elif corner == 3:
		if direction == 'c':
			new_corner = 0
			start, sol_dict = fill_up(start_point, string, sol_dict)
		else:
			new_corner = 2
			start, sol_dict = fill_right(start_point, string, sol_dict)

	return start, sol_dict, new_corner


def fill_right(start, string, sol_dict):
	r, c = start
	if start in sol_dict:
		c += 1
	for i in range(c, c+len(string)):
		sol_dict[(r, i)] = string[i-c]
	return (r, i), sol_dict


def fill_down(start, string, sol_dict):
	r, c = start
	if start in sol_dict:
		r += 1
	for i in range(r, r+len(string)):
		sol_dict[(i, c)] = string[i-r]
	return (i, c), sol_dict


def fill_left(start, string, sol_dict):
	r, c = start
	if start in sol_dict:
		c -= 1
	for i in range(c, c-len(string), -1):
		sol_dict[(r, i)] = string[-(i-c)]
	return (r, i), sol_dict


def fill_up(start, string, sol_dict):
	r, c = start
	if start in sol_dict:
		r -= 1
	for i in range(r, r-len(string), -1):
		sol_dict[(i, c)] = string[-(i-r)]
	return (i, c), sol_dict


def matrixify(dim, sol_dict):
	r, c = dim
	matrix = np.chararray(dim)
	for key in sol_dict:
		matrix[key] = sol_dict[key]
	for i in range(0,r):
		#print(matrix[i,:].decode("utf-8"))
		text_file.write(f'{matrix[i,:].decode("utf-8")}\n')


def dictify(cipher, dim=(3, 16), corner=0, direction='c'):
	r, c = dim
	dict_1 = {}	# should be list but whatever
	i = 0
	count = 0
	if direction == 'c':
		if corner % 2 == 0:
			dict_1 = even_corner(dict_1, count, cipher, r, c, i)
		else:
			dict_1 = odd_corner(dict_1, count, cipher, r, c, i)
	else:
		if corner % 2 == 0:
			dict_1 = odd_corner(dict_1, count, cipher, r, c, i)
		else:
			dict_1 = even_corner(dict_1, count, cipher, r, c, i)

	sol_dict = {}
	count = 0
	grid_count = 0
	if corner == 0:
		start = (0, 0)
	elif corner == 1:
		start = (0, c-1)
	elif corner == 2:
		start = (r-1, c-1)
	elif corner == 3:
		start = (r-1, 0)

	while grid_count < r*c:
		string = dict_1[count]
		start, sol_dict, corner = decide_direction(start, string, sol_dict, corner, direction)
		count += 1
		grid_count += len(string)

	matrixify(dim, sol_dict)


dim_list = []

for i in range(2, int(np.sqrt(len(cipher)))+1):
	factor = len(cipher) / i
	if factor - int(factor) == 0:
		dim_list.append((i, int(factor)))

set_corner = -1
dim = -1
text_file = open("Output.txt", "w")
factor = len(dim_list)

for count in range(0, factor*4):
	set_corner += 1
	if (count % 4) == 0:
		dim += 1
		set_corner = 0
	dictify(cipher, dim=dim_list[dim], corner=set_corner, direction='c')
	text_file.write('\n')
	dictify(cipher, dim=dim_list[dim], corner=set_corner, direction='cc')
	text_file.write('\n')

text_file.close()
