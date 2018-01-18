# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:20:49 2018

@author: theabhishekg
"""

def get_meaning(word):
    from PyDictionary import PyDictionary
    dictionary=PyDictionary()
    return dictionary.meaning(word)