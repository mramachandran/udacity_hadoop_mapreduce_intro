#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is "to find for each student what is the hour during which
# the student has posted the most posts."
# The mapper will just print the 'author_id+hour' of the student as the key and count of 1 against it for each row

#f = '/home/training/udacity_training/data/forum_node.tsv'

import sys
import re
import csv

#for line in csv.reader(open(f,'r'),delimiter="\t"):
for line in csv.reader(sys.stdin,delimiter='\t'):
        data = line           
        datetime  = data[8].split(' ')
        if len(datetime)!=2:
           continue
        else:
           hour = datetime[1][:2] #get the hour component within the datetime
           key = str(data[3]) + str(hour) #concat the hour and the author_id to make the unique key
           print (key+"\t" + str(1)) #produce the mapper output with the key and a count of 1 against it

