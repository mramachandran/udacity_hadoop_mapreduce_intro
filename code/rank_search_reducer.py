#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The reducer takes four inputs - parent id (key), word, 1 and length of each post
# The sort of the mapper makes sure that same parent ids are all following each other that we will use it implicitly
# in the reducer function
# The reducer sorts the posts by word and by length of the post so when searched in a forum, the post having the high score
# based on length for example here will get the first hit. We can always adjust the ranking based on various other criteria
# For example, the goal is to return the post with greater length when searched for hadoop for now. This could be modified
# as we go to improve ranking

import csv
import itertools
import operator
import sys

from operator import itemgetter, attrgetter

#f = 'C:/Users/consultant/Dropbox/udacity/intro to hadoop/forum_node_rank_search.tsv'

def sortdata(x): #sort the records by word and then by length
     if x[0]>y[0]:
       return 1
     elif x[0]==y[0]:
         if x[2]> y[2]:
             return -1
         elif  x[2]==y[2]:
             return 0
         else:
             return 0

     else:  #x < y
       return -1

def accumulate(l):
    answer = ()
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it:
        answer=sortdata(subiter)
        yield (key,answer)

#reducer
data=[]
for line in csv.reader(sys.stdin,delimiter="\t"):
#for line in csv.reader(open(f,'r',encoding='utf8'),delimiter='\t'):

    data.append(line)
    final = data
    final2 = accumulate(final) #aggregation logic happens here which then returns key, (length of the question,avg answer lenght)
    for t1,t2 in final2:
           abs_parent_id = t1
           word = t2[0]
           rank  = t2[1]
           print(abs_parent_id,word,rank)
