import numpy as np


# ---------------------------------------- ENCODE ----------------------------------------

alphabet = 'abcdefghijklmnopqrstuvwxyz'
nyckel = 'ancientxxxpolybius'
adress = 'https://gist.githubusercontent.com/tundal45/3124382/raw/41ba8f67892e533e1cbdbe1a15318608f18be160/output'

matrix = np.array(
    [
        ['a','b','c','d','e'],
        ['f','g','h','i','j'],
        ['k','l','m','n','o'],
        ['p','q','r','s','t'],
        ['u','v','w','x','y'],
    ]
)

nyckel_lista = []
adress_lista = []

for char in nyckel:
    index = alphabet.find(char)
    nyckel_lista.append(alphabet[(index+2) % 26])

nyckel_encoded = ''.join(nyckel_lista)

for char in adress:
    if char in alphabet:
        x, y = np.where(matrix == char)
        adress_lista.append('<'+str(x[0])+str(y[0])+'>')
    else:
        adress_lista.append(char)

adress_encoded = ''.join(adress_lista)

print(nyckel_encoded)
print(adress_encoded)

# ---------------------------------------- DECODE ----------------------------------------
encrypted_key_1 = 'CPEKGPVKPUETKRVKQPUCPFQPGUJQWNFCEEQWPVHQTFCOCIGUTGRCKTU'.lower()
# encrypted_key_1 = 'cpekgv'
encrypted_key_2 = 'rqnadkwu'
encrypted_adress = '<12><34><34><30><33>://<11><13><33><34>.<11><13><34><12><40><01><40><33><04><32><02><24><23><34><04><23><34>.<02><24><22>/<34><40><23><03><00><21>45/3124382/<32><00><42>/41<01><00>8<10>67892<04>533<04>1<02><01><03><01><04>1<00>15318608<10>18<01><04>160/<24><40><34><30><40><34>'

decrypted_key_list = []

for char in encrypted_key_1:
    index = alphabet.find(char)
    decrypted_key_list.append(alphabet[(index-2) % 26])

decrypted_key_list.append(' ') # separate key words

for char in encrypted_key_2:
    index = alphabet.find(char)
    decrypted_key_list.append(alphabet[(index-2) % 26])

decrypted_key = ''.join(decrypted_key_list)

print(decrypted_key)

decrypted_adress_list = []

terminal_count = len(encrypted_adress) - 1
keep_going = True
counter = 0

while True:
    if counter > terminal_count:
        break
    char = encrypted_adress[counter]
    if char == '<':
        x = int(encrypted_adress[counter+1])
        y = int(encrypted_adress[counter+2])
        decrypted_adress_list.append(matrix[x, y])
        counter += 4
    else:
        decrypted_adress_list.append(char)
        counter += 1

decrypted_adress = ''.join(decrypted_adress_list)

# print(decrypted_adress)
