#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is to obtain the top n tags by popularity
# The popularity is simply obtained by the count of occurence of the tag
#
# The general strategy is to create a group of keys (the tag) and for each key
# call the function that sums up the occurences of that tag
# We use iterator to smartly compute grouping and the number of occurences
#
import csv
import itertools
import operator
import sys

from operator import itemgetter, attrgetter

def accumulate(l):
    #create a group of keys and subsets
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it: # for each subset 'yield' key and the len of the list which will be sum
        yield (key,len(list(subiter))) #should be the same as getting the sum of the count as each count is 1


#reducer
data=[]

#use csv.reader to read through the tab delimited data
#create data array by iterating through each line
for line in csv.reader(sys.stdin,delimiter="\t"):
    data.append(line)
final = data
final2 = accumulate(final) #create a set by grouping and aggregating on the subsets
final3 = sorted(final2,key=itemgetter(1),reverse=True) #to obtain the top ten, sort the dataset
#Option --we can try the sort using a function that can create a weight on the time between today's and last activity date
# of the post
for key,count in final3[:10]: #obtain the top 10
           print(key,count)
