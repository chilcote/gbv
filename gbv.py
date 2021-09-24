#!/usr/bin/python3
"""
    Crack open a Milwaukee's Beast, grab some
    college rule from your peechee, and jot down
    some song titles for the album of 26 songs that
    you will spend the next thirteen hours recording.

    Examples:
        Adoptee Yengee Permixture Threadlet
        Unplacable Cirri Whitebelly Shockable Antiabsolutist Stippen
        Figured Coracine Mistranslate Physostegia
        Seedman Tauroctonus Nonelementary Antadiform Eureka
        Agatine Sparver
"""

from random import choice, randint
import sys


def get_words(wordcount, words):
    """Generates a list of words"""
    wordlist = []
    for i in range(1, wordcount):
        wordlist.append(choice(words).lower().strip())
    while True:
        char_count = len(" ".join(wordlist))
        if char_count <= 114:
            break
        wordlist.pop()
    return wordlist


def main():
    with open("/usr/share/dict/words", "r") as f:
        words = f.readlines()
    if len(sys.argv) == 2 and sys.argv[1] == "--password":
        print('_'.join(get_words(4, words)))
    else:
        song_title = ' '.join(get_words(randint(4, 17), words)).title()
        bob_sez = "My favorite GBV song is %s!" % (song_title)
        print(bob_sez)


if __name__ == "__main__":
    main()
