#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the output needs to do two things
# a. make sure we get the most frequent time for each student
# b. capture the ties
# The logic we use here is to use a function to keep the aggregation simple however
# use another complex sort to first sort by key (authorid+hour), then by frequency of the key
# However, to produce the final output - we use a 'if then' to pull the top records for each author we need and
# just ignore the rest

import csv
import sys
import itertools
import operator
import functools
import re


from operator import itemgetter, attrgetter
from itertools import groupby

def mysort(x,y):
    if x[0][0:len(x[0])-2]>y[0][0:len(y[0])-2]:
       return 1
    elif x[0][0:len(x[0])-2]==y[0][0:len(y[0])-2]:
         if x[1]> y[1]:
             return -1
         elif  x[1]==y[1]:
             return 0
         else:
             return 0

    else:  #x < y
       return -1

#reducer
final = ()
oldKey = None
greatestKey = None
thisKey = None
greatestSum = 0
data = []

def accumulate(l):
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it:
       yield key, sum(int(item[1]) for item in subiter)

for line in csv.reader(sys.stdin,delimiter="\t"):
         data.append(line)

final  = data

final2 = accumulate(final)
final3 = sorted(final2,cmp=mysort) # this step is really needed to sort the aggregated output to a desired order
                                   # where we can then apply necessary condition to produce the reducer output

#NOTE: Author+hour is the key
for i,j in final3:
          i = i.strip()
          thisKey = i[:-2] # get the author
          hour =    i[-2:] # hour

          #if the following condition matches - then create the reducer output
          # a. if there is a new key OR
          # b. if there is a old key and the previous count and current count matches
          if (thisKey != oldKey) or (oldKey == thisKey and j==oldCount):
             print (thisKey+"\t" + str(hour))
             oldKey = thisKey
             oldCount = j
