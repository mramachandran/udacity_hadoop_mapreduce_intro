#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is to parse through each tag and print 1 against its occurence so reducer could aggregate
# appropriately
# Format of each line is:
# tagname\t1
# The goal of the program is to compute top n tags.
# The mapper starts with an output of elements - tagname and 1 count against it
# We need to write them out to standard output, separated by a tab
#

import sys
import re
import csv
data1=[]
for line in csv.reader(sys.stdin,delimiter='\t'): #read the tab delimited using csv.reader
    data1.append(line) #create an array with each line
 
for row in data1:
    tags = row[2].strip().split(' ') #obtain the tags that are separated by spaces
    for tag in tags: #for each tag, produce the mapper output
        print(tag + "\t" + "1" )



