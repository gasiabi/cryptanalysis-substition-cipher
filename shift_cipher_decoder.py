# mono-alphabetic substitution cipher
alphabet_small = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś',
                  't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_large = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś',
                  'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

alphabet_small_english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                          'k', 'l', 'm', 'n', 'o', 'p', 'r', 's',
                          't', 'u', 'w', 'y', 'z']
alphabet_large_english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
                          'T', 'U', 'W', 'Y', 'Z']


# generating the key based on the chosen shift
def finding_the_key():

    shift = 2
    key1 = []
    key2 = []

    for i in range(len(alphabet_small_english)):
        new_position = (i + shift) % len(alphabet_small_english)
        key1.append(alphabet_small_english[new_position])

    for i in range(len(alphabet_large_english)):
        new_position = (i + shift) % len(alphabet_large_english)
        key2.append(alphabet_large_english[new_position])

    return key1, key2


def encrypt_the_text(text, key_small, key_large):

    encrypted_text = []

    for letter in text:
        if letter in alphabet_small_english:
            index = alphabet_small_english.index(letter)
            encrypted_text.append(key_small[index])
        elif letter in alphabet_large_english:
            index = alphabet_large_english.index(letter)
            encrypted_text.append(key_large[index])
        else:
            encrypted_text.append(letter)

    final_encrypted_text = ''.join(encrypted_text)

    return final_encrypted_text


# uploading the file and encrypting it
def upload_the_file():
    key_small_1, key_large_2 = finding_the_key()
    file = 'substitute_proprietary.txt'
    new_file = 'decoded.txt'

# utf-8 used to use Polish diacritical marks
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    encrypted_text = encrypt_the_text(text, key_small_1, key_large_2)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()
