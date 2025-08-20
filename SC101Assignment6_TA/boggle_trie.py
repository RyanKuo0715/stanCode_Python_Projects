"""
File: boggle.py
Name: Ryan Kuo
----------------------------------------
Find all possible English vocabularies whose length greater than 4 in the game of Boggle.
"""

from collections import defaultdict
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    Find all possible English vocabularies whose length greater than 4 in the game of Boggle.
    """
    dictionary = defaultdict(list)
    read_dictionary(dictionary)
    words = {}
    input_words(words)

    start = time.time()
    simple_dict = set()
    simplify_dict(simple_dict, dictionary, words)
    get_boggle(simple_dict, words)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(dictionary):
    """
    :param dictionary: list, intended to store all vocabularies in an English dictionary
    :return: list, store all vocabularies in file "dictionary.txt"
    """
    with open(FILE, 'r') as f:
        for line in f:
            if 4 <= len(line.strip()) <= 16:
                dictionary[''.join(sorted(line.strip()))].append(line.strip())


def simplify_dict(simple_dict, dictionary, words):
    """
    :param simple_dict: list, intended to store selected vocabularies
    :param dictionary: list, store all vocabularies in file "dictionary.txt"
    :param words: dict, store all alphabet input by players with their position in boggle
    :return: list, store selected vocabularies with length >= 4 and no more than the number of alphabets in words
    """
    s_word = ''
    for position, word in words.items():
        s_word += word
    s_word = ''.join(sorted(s_word))
    for ele in dictionary:
        if ele[0] in s_word:
            illegal = False
            for ch in ele:
                if ele.count(ch) > s_word.count(ch):
                    illegal = True
                    break
            if not illegal:
                for word in dictionary[ele]:
                    simple_dict.add(word)


def input_words(words):
    """
    :param words: dict, intended to store alphabets input by players
    :return: dict, store all alphabet input by players with their position in boggle
    """
    for i in range(4):
        while True:
            input_letters = input(f'{i+1} row of letters: ')
            input_letter = input_letters.split(' ')
            illegal = False
            if len(input_letter) != 4:
                # eliminate input with alphabets not equal to 4
                print('Illegal input')
                illegal = True
            else:
                for j in range(4):
                    if not input_letter[j].isalpha() or len(input_letter[j]) > 1:
                        # eliminate input other than alphabet or alphabets not separated by white space
                        print('Illegal input')
                        illegal = True
                        break
            if not illegal:
                break
        for j in range(4):
            words[(i, j)] = input_letter[j].lower()


def get_boggle(simple_dict, words):
    """
    :param simple_dict: list, store selected vocabularies with length >= 4 and no more than the number of alphabets in words
    :param words: dict, store all alphabet input by players with their position in boggle
    :return: all vocabularies find in boggle and their total number
    """
    boggle = []
    for position in words:
        get_boggle_helper(position, simple_dict, words, '', [], boggle)
    print(f'There are {len(boggle)} words in total.')


def get_boggle_helper(position, simple_dict, words, find_word, path, boggle):
    """
    :param position: tuple, the coordinate of an alphabet in the boggle
    :param simple_dict: list, store selected vocabularies with length >= 4 and no more than the number of alphabets in words
    :param words: dict, store all alphabet input by players with their position in boggle
    :param find_word: str, the word that has been combined in recursion
    :param path: list, the coordinate of alphabets that have been searched in recursion
    :param boggle: list, valid vocabularies that have been found in recursion
    :return: list, valid vocabularies that have been found in recursion
    """
    if position in path or not has_prefix(simple_dict, find_word):
        # base case 1: coordinate that has been searched
        # base case 2: the word that has been found does not exist in dictionary
        pass
    else:
        # choose
        find_word += words[position]
        path.append(position)
        # explore
        if has_prefix(simple_dict, find_word):
            if find_word in simple_dict and find_word not in boggle:
                boggle.append(find_word)
                print(f'Found "{find_word}"')
            for i in range(max(0, position[0]-1), min(4, position[0]+2)):
                for j in range(max(0, position[1]-1), min(4, position[1]+2)):
                    if (i, j) not in path and (i, j) != position:
                        get_boggle_helper((i, j), simple_dict, words, find_word, path, boggle)
        # un-choose
        path.pop()  # or use path.copy() in get_boogle_helper(), a suggestion from ChatGPT


def has_prefix(simple_dict, find_word):
    """
    :param simple_dict: list, store selected vocabularies with length >= 4 and no more than the number of alphabets in words
    :param find_word: str, the word that has been combined in recursion
    :return: bool, whether find_string fits vocabularies in simple_dict
    """
    for word in simple_dict:
        if word.startswith(find_word):
            return True
    return False


if __name__ == '__main__':
    main()
