#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is "to see if there are already students on forums that communicate a lot between themselves."
# The approach we have is to obtain the abs_parent_id of any post and print out the author id next to it and
# let the reducer figure out how to produce the output
# abs_parent_id is the id that will give the root id of any post - irrespective of whatever depth the post is

import sys
import re
import csv

data1=[]
#read the tab delimited file
#add the line to an array
for line in csv.reader(sys.stdin,delimiter='\t'):
    data1.append(line)
 
for row in data1: #for each item in the array produce the correct mapper output
    author_id = row[3]
    abs_parent_id = row[7]
    parent_id = row[6]
    id = row[0]
    if author_id == 'author_id': #we need to exclude the first line
       continue
    if abs_parent_id=="\\N": #if there is no abs_parent_id - or no parent at all, then use the id of the report as its parent
       abs_parent_id = id

    print( str(abs_parent_id) + "\t" + author_id) #produce the output


