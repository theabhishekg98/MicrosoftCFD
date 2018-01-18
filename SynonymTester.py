# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:13:30 2018

@author: theabhishekg
"""


def word_synonym_tester():
    import random
    import csv

    fil = open('wordlist.csv')
    csv_f = csv.reader(fil)

    # converting csv_f to list
    my_csv_word = list(csv_f)

    # choosing random word and its meaning from the list
    q_p = random.randint(1, 1163)
    q_word = my_csv_word[q_p][0]
    q_meaning = my_csv_word[q_p][1]

    # creating an empty option list
    option_list = []

    # finding position of correct synonym to assure diff positions every time it's called
    correct_word_pos = random.randint(0, 3)

    # generating the synonym for q_word
    from nltk.corpus import wordnet
    synonyms = wordnet.synsets(q_word)
    correct_word = synonyms[0].name().split(".")[0]  # taking the first one as it generates a string of words

    # jumbling the words into a list
    for x in range(0, 4):
        a = random.randint(1, 1163)
        if x != correct_word_pos:
            option_list.append(my_csv_word[a][0])
        elif x == correct_word_pos:
            option_list.append(correct_word)

    return q_word, q_meaning, option_list[0], option_list[1], option_list[2], option_list[3], correct_word
