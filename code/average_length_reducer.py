#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The reducer takes three inputs - parent id (key), node type (answer or question), and length of each post
# The sort of the mapper makes sure that same parent ids are all following each other that we will use it implicitly
# in the reducer function
#
import csv
import itertools
import operator
import sys

f = '/home/training/udacity_training/data/forum_node_output.tsv'
from operator import itemgetter, attrgetter


def computeQLenAndAnswerAvgLength(x):
    avg = 0
    count = 0
    sum = 0
    questionLength = 0
    #print(x)
    
    for item in x:
        if item[1] == 'answer': # if it is answer we just need to total it and keep the count for average
            sum = sum + int(item[2])
            count+=1
        else:
            if item[1] == 'question': # itis question ,i am assuming that there is only one and therefore just use that length
               questionLength = int(item[2])

    if sum == 0:
       return (questionLength,0) # make sure we don't divide by zero
    else:
       return (questionLength,sum/count)

def accumulate(l):
    answer = ()
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it:
        answer=computeQLenAndAnswerAvgLength(subiter)
        yield (key,answer)

#reducer
data=[]

for line in csv.reader(sys.stdin,delimiter="\t"):
    data.append(line)
final = data
final2 = accumulate(final) #aggregation logic happens here which then returns key, (length of the question,avg answer lenght)
for t1,t2 in final2:
           key = t1
           QLength = t2[0]
           AvgAnswerLength  = t2[1]
           print(key,QLength,AvgAnswerLength)
