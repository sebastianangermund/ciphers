import matplotlib.pyplot as plt

from cipher_list import cipher_list_2 as cipher_list



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

def plot_frequency(frequency_hist):
    X = [letter for letter in frequency_hist.keys()]
    Y = [value for _, value in frequency_hist.items()]
    X.reverse()
    Y.reverse()
    Y_norm = []
    max = Y[0]
    for val in Y:
        Y_norm.append(val/max)
    plt.bar(X, Y_norm)
    plt.savefig('dist.png', bbox_inches='tight')

def english_frequency_sub(cipher, alphabet):
    eng_letter_freq = "etaoinshrdlcumwfgypbvkjxqz"
    sorted_hist = get_sorted_letter_frequency(cipher, alphabet)
    sorted_letters = [letter for letter in sorted_hist.keys()]
    sorted_letters.reverse()
    conversion_dict = dict(zip(sorted_letters, eng_letter_freq))
    # i - h
    # 
    conversion_dict_modified = {
        'n': 'a',
        'i': 'b',
        'w': 'c',
        'd': 'd',
        'e': 'e',
        'k': 'f',
        'u': 'g',
        'b': 'h',
        'l': 'i',
        'j': 'j',
        'v': 'k',
        'm': 'l',
        'x': 'm',
        't': 'n',
        'r': 'o',
        'f': 'p',
        'q': 'q',
        'p': 'r',
        'c': 's',
        's': 't',
        'a': 'u',
        'h': 'v',
        'o': 'w',
        'y': 'x',
        'g': 'y',
        'z': 'z'
    }
    decrypted = ''
    for letter in cipher:
        if letter in alphabet:
            decrypted += conversion_dict_modified[letter]
        else:
            decrypted += letter
    print(decrypted)

def write_all_ceasar_subs_to_file(cipher, alphabet):
    for index in range(1, (len(alphabet)+1)):
        decrypted = ''
        for letter in cipher:
            if letter in alphabet:
                decrypted += alphabet[(alphabet.find(letter)+index) % len(alphabet)]
            else:
                decrypted += letter
        with open('substitutions.txt', 'a') as f:
            f.write(f'\n\n{decrypted}')

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ' '.join(cipher_list)
    sorted_hist = get_sorted_letter_frequency(cipher, alphabet)
    plot_frequency(sorted_hist)



if __name__ == '__main__':
    main()