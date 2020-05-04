from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
import time

def cleanInput(input):
    input = re.sub('\n', '', input).lower()
    input = re.sub('\[[0 - 9]+\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        print(item)
        time.sleep(1)
        item = item.strip(string.punctuation)
        print(item)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = " ".join(input[i : i + n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
print(ngrams.items())
time.sleep(10)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse = True) # for dictionary sorting / axis = key / value (itemgetter(number))
print(sortedNGrams)