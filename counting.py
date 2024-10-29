# This program analyzes the frequency of each letter in the uploaded text.
# It was designed for cryptographic analysis of encoded texts.

dictionary_alphabet = {
    'a': 0, 'ą': 0, 'b': 0, 'c': 0, 'ć': 0, 'd': 0,
    'e': 0, 'ę': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    'j': 0, 'k': 0, 'l': 0, 'ł': 0, 'm': 0, 'n': 0,
    'ń': 0, 'o': 0, 'ó': 0, 'p': 0, 'r': 0, 's': 0,
    'ś': 0, 't': 0, 'u': 0, 'w': 0, 'y': 0, 'z': 0,
    'ź': 0, 'ż': 0, 'q': 0, 'x': 0, 'v': 0
}


def upload_the_file():
    file = 'substitute_proprietary.txt'

    with open(file, 'r') as f:
        text = f.read()

    return text


def counting():
    text = upload_the_file()
    for y in text:
        if y in dictionary_alphabet:
            dictionary_alphabet[y] += 1
        else:
            continue
    return dictionary_alphabet


if __name__ == '__main__':
    final_dictionary = counting()
    for x in final_dictionary:
        print(x, ":", final_dictionary[x])
