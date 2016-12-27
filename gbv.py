#!/usr/bin/python
'''
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
'''

from random import choice, randint

def get_songtitle(wordcount, words):
    '''Generates a string of given length (wordcount), using Title Case.'''
    songtitle = []
    for i in range(1, wordcount):
        songtitle.append(choice(words).title().strip())
    while True:
        char_count = len(' '.join(songtitle))
        if char_count <= 114:
            break
        songtitle.pop()
    return ' '.join(songtitle)

def main():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.readlines()
    bob_sez = 'My favorite GBV song is %s!' % get_songtitle(randint(4, 17), words)
    print bob_sez

if __name__ == "__main__":
    main()
