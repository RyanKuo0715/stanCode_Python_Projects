"""
File: anagram.py
Name: Hsinhuihuang
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

# import time                   # This file allows you to calculate the speed of your algorithm
#
# # Constants
# FILE = 'dictionary.txt'       # This is the filename of an English dictionary
# EXIT = '-1'                   # Controls when to stop the loop
#
#
# def main():
#     print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
#     dictionary = read_dictionary()
#     while True:
#         word = input("Find anagrams for: ")
#         if word == EXIT:
#             break
#         start = time.time()
#         find_anagrams(word, dictionary)
#         end = time.time()
#         print('----------------------------------')
#         print(f'The speed of your anagram algorithm: {end-start} seconds.')
#
#
# def read_dictionary():
#     with open(FILE, 'r') as f:
#         return [word.strip() for word in f.readline()]
#
#
# def find_anagrams(s, dictionary):
#     anagrams = []
#     print("Searching...")
#     find_anagrams_helper(s, '', dictionary, anagrams, set())
#     print(f"{len(anagrams)} anagrams: {anagrams}")
#
#
# def find_anagrams_helper(s, current, dictionary, anagrams, used_indices):
#     if len(current) == len(s) and current in dictionary and current not in anagrams:
#         anagrams.append(current)
#         print(f"Found: {current}")
#     else:
#         for i in range(len(s)):
#             if i not in used_indices:
#                 # Choose
#                 used_indices.add(i)
#                 current += s[i]
#                 if has_prefix(current, dictionary):
#                     # Explore
#                     find_anagrams_helper(s, current, dictionary, anagrams, used_indices)
#                 # Unchoose
#                 current = current[:-1]
#                 used_indices.remove(i)
#
#
# def has_prefix(sub_s, dictionary):
#     return any(word.startswith(sub_s) for word in dictionary)
#
#
# if __name__ == '__main__':
#     main()

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    dictionary, prefixes = read_dictionary()  # Unpack both sets
    while True:
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        start = time.time()
        find_anagrams(word, dictionary, prefixes)  # Pass prefixes here
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        dictionary = set(word.strip() for word in f.readlines())
    prefixes = set()
    for word in dictionary:
        for i in range(len(word)):
            prefixes.add(word[:i + 1])
    return dictionary, prefixes


def find_anagrams(s, dictionary, prefixes):
    anagrams = []
    print("Searching...")
    find_anagrams_helper(s, '', dictionary, anagrams, set(), prefixes)  # Removed memo, added prefixes
    print(f"{len(anagrams)} anagrams: {anagrams}")


def find_anagrams_helper(s, current, dictionary, anagrams, used_indices, prefixes):
    if len(current) == len(s) and current in dictionary and current not in anagrams:
        anagrams.append(current)
        print(f"Found: {current}")
    else:
        for i in range(len(s)):
            if i not in used_indices:
                # Choose
                used_indices.add(i)
                current += s[i]
                if has_prefix(current, prefixes):  # Removed memo argument
                    # Explore
                    find_anagrams_helper(s, current, dictionary, anagrams, used_indices, prefixes)  # Passed prefixes
                # Unchoose
                current = current[:-1]
                used_indices.remove(i)


def has_prefix(sub_s, prefixes):
    return sub_s in prefixes


if __name__ == '__main__':
    main()
