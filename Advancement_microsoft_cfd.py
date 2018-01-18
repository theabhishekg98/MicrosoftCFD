# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:10:45 2018

@author: theabhishekg
"""

#import nltk
#nltk.download()

#def get_without_stopword('Hello tester, I am abhishek'):

def get_without_stopword(arg):    
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import string
    
    user_input_wordsplit = word_tokenize(arg)
    
    #make a copy of the user_input_wordsplit
    filtered_word_list = user_input_wordsplit
    
    #remove punctuation
    filtered_word_list = [''.join(c for c in s if c not in string.punctuation) for s in filtered_word_list]

    #remove empty strings    
    filtered_word_list = [s for s in filtered_word_list if s]
    
    #iterate over user_input_wordsplit
    for word in user_input_wordsplit: 
      if word in stopwords.words('english'): 
        filtered_word_list.remove(word)
    
    return filtered_word_list