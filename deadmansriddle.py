import matplotlib.pyplot as plt
import multiprocessing as mp

import time

from random import randint
from pprint import pprint
from itertools import permutations

from cipher_list import cipher_list_4lw as cipher_list



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


def get_sorted_word_frequency(cipher):
    hist = {}
    for word in cipher.split(' '):
        if word in hist.keys():
            hist[word] += 1
        else:
            hist[word] = 1
    hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1])}
    return hist


def plot_frequency(frequency_hist):
    X = [letter for letter in frequency_hist.keys()]
    Y = [value for _, value in frequency_hist.items()]
    print(X)
    print(Y)
    plt.plot(X.reverse(), Y.reverse())
    plt.savefig('word_frequency.png', bbox_inches='tight')


def get_letter_frequency_conversion(cipher_letter_freq, given_letter_freq):
    sorted_letters = [letter for letter in cipher_letter_freq.keys()]
    sorted_letters.reverse()
    conversion_dict = dict(zip(sorted_letters, given_letter_freq))
    return conversion_dict


def conversion_dict_sub(cipher, conversion_dict, alphabet):
    decrypted = ''
    for letter in cipher:
        if letter in alphabet:
            decrypted += conversion_dict[letter]
        else:
            decrypted += letter
    return decrypted


def brute_force_permutations(conversion_dict, keys_keep_constant=[]):
    conversion_dicts = []
    keys = []
    values = []
    for key, value in conversion_dict.items():
        keys.append(key)
        values.append(value)
    for index, key in enumerate(keys):
        new_dict = conversion_dict.copy()
        if key in keys_keep_constant:
            continue
        if (index % 2) == 0:
            continue
        if key == keys[-1]:
            break
        tmp_val = conversion_dict[key]
        new_dict[key] = values[index+1]
        new_dict[keys[index+1]] = tmp_val
        conversion_dicts.append(new_dict)
    return conversion_dicts


def permutate_letter_freq(letters):
    new_freq = 'eta'
    # new_freq = 'eao'
    letters = letters[3:]
    end_index = len(letters) -1
    for index in range(end_index): # ignoring last
        while True:
            if index == 0:
                new_letter = letters[randint(0,1)]
                if new_letter in new_freq:
                    continue
                new_freq += new_letter
                break
            elif index == end_index:
                new_letter = letters[randint(end_index-1,end_index)]
                if new_letter in new_freq:
                    continue
                new_freq += new_letter
                break
            else:
                new_letter = letters[randint((index-1),(index+1))]
                if new_letter in new_freq:
                    continue
                new_freq += new_letter
                break
    return new_freq


def brute_force_random(letter_freq, common_words, runs=1):
    alphabet = "abcdefghijklmnopqrstuvwxy"
    cipher = ' '.join(cipher_list)
    sorted_word_freq = get_sorted_word_frequency(cipher)
    cipher_unique = ' '.join(sorted_word_freq.keys())
    sorted_letter_freq = get_sorted_letter_frequency(cipher, alphabet)
    letter_freq_cache = {}
    ###
    T = []
    Y = []
    ###
    for index in range(runs):
        ###
        if (index % 1000 == 0):
            start = time.perf_counter()
        ###
        while True:
            permutated_letter_freq = permutate_letter_freq(letter_freq)
            if permutated_letter_freq in letter_freq_cache.keys():
                continue
            letter_freq_cache[permutated_letter_freq] = index
            break
        ###
        if start:
            end_time = time.perf_counter() - start
            T.append(end_time)
            Y.append(len(letter_freq_cache))
            print(T)
            print(Y)
            start = None
        ###
        conversion_dict = get_letter_frequency_conversion(sorted_letter_freq, permutated_letter_freq)
        pprint(conversion_dict)
        decrypted = conversion_dict_sub(cipher_unique, conversion_dict, alphabet)
        for word in decrypted.split(' '):
            if word in common_words:
                decrypted = conversion_dict_sub(cipher, conversion_dict, alphabet)
                with open('brute_force.txt', 'a') as f:
                    f.write(f'\n\n{decrypted}')
                break


def brute_force_multi(permutations_):
    letter_freq   = "etaoinshrd"
    alphabet = "abcdefghijklmnopqrstuvwxy"
    common_words = ['that', 'this', 'with', 'list', 'have', 'from', 'they', 'when',
                        'give', 'find', 'must', 'your', 'time', 'what', 'only', 'were',
                        'more', 'about', 'other', 'first', 'would', 'price',
                        'the', 'and', 'for', 'not', 'are']
    vals = [0]*(len(common_words_eng))
    common_words = dict(zip(common_words, vals))
    cipher = ' '.join(cipher_list)
    sorted_word_freq = get_sorted_word_frequency(cipher)
    cipher_unique = ' '.join(sorted_word_freq.keys())
    sorted_letter_freq = get_sorted_letter_frequency(cipher, alphabet)
    permutations_ = permutations(letter_freq)
    return_list = []
    for permutation in permutations_:
        permutation = ''.join(permutation)
        permutation_plus = permutation + 'lcumwfgypbvkjxq'
        conversion_dict = get_letter_frequency_conversion(sorted_letter_freq, permutation_plus)
        decrypted = conversion_dict_sub(cipher_unique, conversion_dict, alphabet)
        word_matches = []
        for word in decrypted.split(' '):
            if word in common_words.keys():
                word_matches.append(word)
            if len(word_matches) == 4:
                decrypted = conversion_dict_sub(cipher, conversion_dict, alphabet)
                return_list.append(word_matches, decrypted)
                print('match')
                break

if __name__ == '__main__':
    # everything is straight forward except method "permutate_letter_freq"
    # which is highly speculative
    # letter_freq_eng = "etaoinshrdlcumwfgypbvkjxq"
    letter_freq_eng   = "etaoinshrd"
    letter_freq_span = "eaosrindlctumpbgyvqhfzj"
    common_words_span = ['como', 'para', 'ellos', 'tener', 'este', 'desde', 'pero', 'algunos',
                         'usted', 'tenido', 'lata', 'fuera', 'otros', 'eran', 'hacer', 'como',
                         'cada', 'decir', 'hace', 'tres', 'aire', 'jugar', 'poner', 'casa']
    common_words_eng = ['that', 'this', 'with', 'list', 'have', 'from', 'they', 'when',
                        'give', 'find', 'must', 'your', 'time', 'what', 'only', 'were',
                        'more', 'about', 'other', 'first', 'would', 'price',
                        'the', 'and', 'for', 'not', 'are']
    vals = [0]*(len(common_words_eng))
    common_words_eng = dict(zip(common_words_eng, vals))
    permutations_ = permutations(letter_freq_eng)
    with mp.Pool(8) as p:
        result_list = p.map(brute_force_multi, permutations_)

    for element in result_list:
        print(element)

    # runs = 1
    # brute_force_random(letter_freq_eng, common_words_eng, runs)
