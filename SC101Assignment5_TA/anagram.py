"""
File: anagram.py
Name: Ryan Kuo
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# note: count characters in a string
# https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string


import time                   # This file allows you to calculate the speed of your algorithm
from collections import defaultdict

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


# def main():
#     """
#     fina anagrams of a vocabulary
#     """
#     dictionary = []
#     read_dictionary(dictionary)
#     while True:
#         print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
#         vocabulary = input('Find anagrams for: ')
#         start = time.time()
#         if vocabulary == EXIT:  # exit the program
#             break
#         else:  # conduct anagram searching
#             print('Searching...')
#             simple_dict = []
#             simplify_dictionary(simple_dict, dictionary, vocabulary.lower())
#             find_anagrams(vocabulary.lower(), simple_dict)
#         end = time.time()
#         print('----------------------------------')
#         print(f'The speed of your anagram algorithm: {end-start} seconds.')
#         print('')
#
#
# def read_dictionary(dictionary):
#     """
#     :param dictionary: lst, an empty list to store vocabularies
#     :return: lst, a list with all vocabularies copied from an English dictionary
#     """
#     with open(FILE, 'r') as f:
#         for line in f:
#             dictionary.append(line.strip())
#
#
# def simplify_dictionary(simple_dict, dictionary, vocabulary):
#     """
#     :param simple_dict: lst, an empty list to store selected vocabularies
#     :param dictionary: lst, a list with all vocabularies copied from an English dictionary
#     :param vocabulary: str, a vocabulary whose anagrams are intended to be searched
#     :return: lst, a list with selected vocabularies which have as same length as that of
#         vocabulary and only contain characters that vocabulary contains
#     """
#     for word in dictionary:
#         if word[0] in vocabulary:  # raise the speed
#             if len(word) == len(vocabulary) and set(word) == set(vocabulary):  # set(word)：生成dict，儲存word裡面出現的單字
#                 simple_dict.append(word)
#
#
# def find_anagrams(string, simple_dict):
#     """
#     :param string: str, a vocabulary whose anagrams are intended to be searched
#     :param simple_dict: lst, a list with selected vocabularies
#     :return: anagrams of the vocabulary
#     """
#     anagram = []
#     find_anagrams_helper(string, '', simple_dict, anagram)
#     print(f'{len(anagram)} anagrams: {anagram}')
#
#
# def find_anagrams_helper(string, find_string, simple_dict, anagram):
#     """
#     :param string: str, a vocabulary whose anagrams are intended to be searched
#     :param find_string: str, a string created in recursion to find anagrams
#     :param simple_dict: lst, a list with selected vocabularies
#     :param anagram: lst, a list contains anagrams that have been found
#     :return: anagrams of the vocabulary that have been found
#     """
#     if len(find_string) == len(string):
#         if has_prefix(find_string, simple_dict):
#             anagram.append(find_string)
#             print(f'Found: {find_string}')
#             print('Searching...')
#     else:
#         for ch in string:
#             if find_string.count(ch) < string.count(ch):
#                 # choose
#                 find_string += ch
#                 # explore
#                 if not has_prefix(find_string, anagram) and has_prefix(find_string, simple_dict):
#                     # if not has_prefix(find_string, anagram):
#                     #     to avoid the anagram that has been found
#                     # if has_prefix(find_string, simple_dict):
#                     #     to make sure there is a word in simple_dict starts with find_string
#                     find_anagrams_helper(string, find_string, simple_dict, anagram)
#                 # un-choose
#                 find_string = find_string[:-1]
#
#
# def has_prefix(find_string, simple_dict):
#     """
#     :param find_string: str, a string created in recursion to find anagrams
#     :param simple_dict: lst, a list with selected vocabularies
#     :return: bool, whether find_string fits vocabularies in simple_dict
#     """
#     for word in simple_dict:
#         if word.startswith(find_string):
#             return True
#     return False


def main():
    """
    fina anagrams of a vocabulary
    """
    dictionary = defaultdict(list)
    read_dictionary(dictionary)
    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        vocabulary = input('Find anagrams for: ')
        start = time.time()
        if vocabulary == EXIT:  # exit the program
            break
        else:  # conduct anagram searching
            print('Searching...')
            simple_dict = set()
            simplify_dictionary(simple_dict, dictionary, vocabulary.lower())
            find_anagrams(vocabulary.lower(), simple_dict)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        print('')


def read_dictionary(dictionary):
    """
    :param dictionary: lst, an empty list to store vocabularies
    :return: lst, a list with all vocabularies copied from an English dictionary
    """
    with open(FILE, 'r') as f:
        for line in f:
            dictionary[tuple(sorted(set(line.strip())))].append(line.strip())


def simplify_dictionary(simple_dict, dictionary, vocabulary):
    """
    :param simple_dict: lst, an empty list to store selected vocabularies
    :param dictionary: lst, a list with all vocabularies copied from an English dictionary
    :param vocabulary: str, a vocabulary whose anagrams are intended to be searched
    :return: lst, a list with selected vocabularies which have as same length as that of
        vocabulary and only contain characters that vocabulary contains
    """
    for word in dictionary[tuple(sorted(set(vocabulary)))]:
        if len(word) == len(vocabulary):
            simple_dict.add(word)


def find_anagrams(string, simple_dict):
    """
    :param string: str, a vocabulary whose anagrams are intended to be searched
    :param simple_dict: lst, a list with selected vocabularies
    :return: anagrams of the vocabulary
    """
    anagram = []
    find_anagrams_helper(string, '', simple_dict, anagram)
    print(f'{len(anagram)} anagrams: {anagram}')


def find_anagrams_helper(string, find_string, simple_dict, anagram):
    """
    :param string: str, a vocabulary whose anagrams are intended to be searched
    :param find_string: str, a string created in recursion to find anagrams
    :param simple_dict: lst, a list with selected vocabularies
    :param anagram: lst, a list contains anagrams that have been found
    :return: anagrams of the vocabulary that have been found
    """
    if len(find_string) == len(string):
        anagram.append(find_string)
        print(f'Found: {find_string}')
        print('Searching...')
    else:
        for ch in string:
            if find_string.count(ch) < string.count(ch):
                # choose
                find_string += ch
                # explore
                if not has_prefix(find_string, anagram) and has_prefix(find_string, simple_dict):
                    find_anagrams_helper(string, find_string, simple_dict, anagram)
                # un-choose
                find_string = find_string[:-1]


def has_prefix(find_string, simple_dict):
    """
    :param find_string: str, a string created in recursion to find anagrams
    :param simple_dict: lst, a list with selected vocabularies
    :return: bool, whether find_string fits vocabularies in simple_dict
    """
    for word in simple_dict:
        if word.startswith(find_string):
            return True
    return False


if __name__ == '__main__':
    main()
