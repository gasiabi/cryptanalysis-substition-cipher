# This program searches for words of a specified length in the uploaded text.
# It is intended for cryptographic analysis of encoded texts.

import re


def upload_the_file():
    file = 'substitute_proprietary.txt'

    with open(file, 'r') as f:
        text = f.read()

    # Getting rid of the symbols
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    words = cleaned_text.split()
    return words


def counting(length):
    found_words = []
    words = upload_the_file()

    # Finding the words of the specific length
    for x in words:
        if len(x) == length:
            found_words.append(x)

    return found_words


if __name__ == '__main__':
    print(counting(5))
