#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is to eventually find out whether
# there is a produce an output that is going to be fed to the reducer to help associate
# words in the input to a particular post based on a ranking system primarily now focussed on length of the post

import sys
import re
import csv
#f = 'C:/Users/consultant/Dropbox/udacity/intro to hadoop/forum_node.tsv'
#f1 = 'C:/Users/consultant/Dropbox/udacity/intro to hadoop/forum_node_rank_search.tsv'

data1=[]

#with open(f1,'w',encoding='utf8') as tcsvout:
 #for line in csv.reader(open(f,'r',encoding='utf8'),delimiter='\t'):
for line in csv.reader(sys.stdin,delimiter='\t'):
    data1.append(line)

for data in data1:
     line = data[4].strip('<p>').strip('][')
     words = re.split('\W+',line)
     #print(words)
     body = data[4]
     abs_parent_id = data[7]
     id = data[0]

     if abs_parent_id == "\\N":
        abs_parent_id = id # if there is no parent id then set id to be the parent id

     for word in words:
         print(abs_parent_id  + "\t" + word + "\t1\t" + str(len(body)))

         #sample output - post id, word, 1, 59

