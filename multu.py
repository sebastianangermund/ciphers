
import multiprocessing as mp

from itertools import permutations

from cipher_list import cipher_list_4lw as cipher_list


def get_sorted_word_frequency(cipher):
    hist = {}
    for word in cipher.split(' '):
        if word in hist.keys():
            hist[word] += 1
        else:
            hist[word] = 1
    hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1])}
    return hist


def get_sorted_letter_frequency(cipher, alphabet):
    hist = {}
    for letter in cipher:
        if letter not in alphabet:
            continue
        elif letter in hist.keys():
            hist[letter] += 1
        else:
            hist[letter] = 1
    hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1])}
    return hist


def conversion_dict_sub(cipher, conversion_dict, alphabet):
    decrypted = ''
    for letter in cipher:
        if letter in alphabet:
            decrypted += conversion_dict[letter]
        else:
            decrypted += letter
    return decrypted


def get_letter_frequency_conversion(cipher_letter_freq, given_letter_freq):
    sorted_letters = [letter for letter in cipher_letter_freq.keys()]
    sorted_letters.reverse()
    conversion_dict = dict(zip(sorted_letters, given_letter_freq))
    return conversion_dict


def brute_force_multi(permutations_):
    return_list = []
    for permutation in permutations_:
        permutation = ''.join(permutation)
        permutation_plus = permutation + 'hrdlcumwfgypbvkjxq'
        print(permutation_plus)
        conversion_dict = get_letter_frequency_conversion(sorted_letter_freq, permutation_plus)
        decrypted = conversion_dict_sub(cipher_unique, conversion_dict, alphabet)
        word_matches = []
        for word in decrypted.split(' '):
            if word in common_words.keys():
                word_matches.append(word)
            if len(word_matches) == 2:
                decrypted = conversion_dict_sub(cipher, conversion_dict, alphabet)
                return_list.append(word_matches, decrypted)
    return return_list


alphabet = "abcdefghijklmnopqrstuvwxy"
letter_freq   = "etaoins"
common_words = ['that', 'this', 'with', 'list', 'have', 'from', 'they', 'when',
                'give', 'find', 'must', 'your', 'time', 'what', 'only', 'were',
                'more', 'about', 'other', 'first', 'would', 'price',
                'the', 'and', 'for', 'not', 'are']
vals = [0]*(len(common_words))
common_words = dict(zip(common_words, vals))
permutations_ = permutations(letter_freq)


cipher = ' '.join(cipher_list)
sorted_word_freq = get_sorted_word_frequency(cipher)
cipher_unique = ' '.join(sorted_word_freq.keys())
sorted_letter_freq = get_sorted_letter_frequency(cipher, alphabet)

# multi
with mp.Pool(8) as p:
    result_list = p.map(brute_force_multi, [''.join(perm) for perm in permutations_])

# normal
# result_list = brute_force_multi(permutations_)

for element in result_list:
    print(element)