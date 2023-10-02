import configparser
import pandas as pd
from datetime import datetime
from pynytimes import NYTAPI
import string
import re

def show_alliteration(words):

    """ added 'and' to the stop words """
    stop_words = ["i", "a", "about", "an", "and", "are", "as", "at", "be", "by", 
                  "com", "for", "from", "how", "in", "is", "it", "of", "on", 
                  "or", "that", "the", "this", "to", "was", "what", "when", 
                  "where", "who", "will", "with", "the"]
    words.reverse()
    prev_word = "."
    alliteration_list = []
    first_time = True
    while len(words):
        word = words.pop()
        word = word.translate(str.maketrans('','', string.punctuation))
        pair = ['', '']
        if word.lower() not in stop_words and word != '' and not re.match('^[0-9]+$', word):
            if word[0].lower() == prev_word[0].lower():
                if first_time == True:
                    pair[0] = prev_word
                    first_time = False
                if pair not in alliteration_list:
                    pair[1] = word
                    if pair[0] != '' and pair[1] != '':
                        pair = tuple(pair)
                        alliteration_list.append(pair)
            prev_word = word

    return alliteration_list


def get_nimes(yearmonth):
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    API_KEY = config['nytimes']['API_KEY']
    df = pd.DataFrame()
    
    nyt = NYTAPI(API_KEY, parse_dates=True)

    month = yearmonth.split('-')

    data = nyt.archive_metadata(
        date = datetime(int(month[0]), int(month[1]), 1)
    )

    df = pd.json_normalize(data, sep='')
    df['nimes'] = ''

    alist = []
    idx = 0
    for article in data:
        nice = show_alliteration(article['headline']['main'].split()) 
        if nice != []:
            nimes = []
            for tup in nice:
                alist.append(tup)
                hlist = list(tup)
                nimes.append(f"{hlist[0]} {hlist[1]}")
            if nimes != []:
                df.at[idx, 'nimes'] = ', '.join(nimes)
            idx += 1

    newlist = list(set(alist))
    newlist.sort()
    nimeslist = []

    if newlist != []:
        for tup in newlist:
            hlist = list(tup)
            nimeslist.append(f"{hlist[0]} {hlist[1]}")

    return nimeslist