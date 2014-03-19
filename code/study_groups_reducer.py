#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal is "that for each forum thread (that is a question node with all it's answers and comments)
# would give us a list of students that have posted there
# The approach we have taken is to group the mapper output by each forum's abs_parent_id and then for each subitem
# concatenate the author ids related to that post and its 'children' -answers, comments
# The approach is to use python's grouping functionality

import csv
import itertools
import operator
import sys

from operator import itemgetter, attrgetter

def accumulate(l):
    answer = ()
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it:
        answer = contactConnects(subiter)
        yield key,answer

def contactConnects(x):
    answer=()
    connections=[]
    for item in x:
        connections.append(item[1]) #item1 will have the author id

    return connections


#reducer
data=[]
#read the tab delimited file
#add the line to an array
for line in csv.reader(sys.stdin,delimiter="\t"):
    data.append(line)
final = data


# the main this happening on this program is this accumulate function
final2 = accumulate(final)
for key,connections in final2:
    print(key,connections)
