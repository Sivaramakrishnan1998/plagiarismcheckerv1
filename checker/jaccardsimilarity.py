
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import math

def twoCharGram(dataset):
    with open(dataset, 'r') as data:
        textFile = data.read().replace('\n', ' ')
        kGrams = set()
        # 2-Char gram
        for i in range(len(textFile)-1):
            if textFile[i] + textFile[i+1] not in kGrams:
                kGrams.add(textFile[i] + textFile[i+1])
    return kGrams


# Ex. "I am Sam" = { ['I a'], [' am'], ['am '], ['m S'], [' Sa'], ['Sam']}
def threeCharGram(dataset):
    with open(dataset, 'r') as data:
        textFile = data.read().replace('\n', ' ')
        kGrams = set()
        # 3-Char gram
        for i in range(len(textFile)-2):
            if textFile[i] + textFile[i+1] + textFile[i+2] not in kGrams:
                kGrams.add(textFile[i] + textFile[i+1] + textFile[i+2])
    return kGrams


# Ex. "I am Sam" = { ['I am'], ['am Sam']}
def twoWordGram(dataset):
    with open(dataset, 'r') as data:
        tokens = str.split(data.read().replace('\n', ' '))
        kGrams = set()
        #2-word gram
        for i in range(len(tokens)-1):
            if tokens[i] + ' ' + tokens[i+1] not in kGrams:
                kGrams.add(tokens[i] + ' ' + tokens[i+1])
    return kGrams

def jaccard(d1,d2, message):
    print('D1.txt\'s '+ message +' similarity with D2.txt is: %.6f percent' % (100.* len(D1set.intersection(D2set))/ len(D1set.union(D2set))))
    


D1set = threeCharGram('D1.txt')
D2set = threeCharGram('D2.txt')

jaccard(D1set,D2set, 'two char gram')