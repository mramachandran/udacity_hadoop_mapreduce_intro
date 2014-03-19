#!/usr/bin/python
__author__ = 'Manoj Ramachandran'
# The goal of the program is to eventually find out whether
# there is a correlation between the length of a post and the length of answers
# To start with, we simply produce a mapper output of parent_id, node_type and length of each post
# The node_type will be either 'answer' or 'question' which we will then use in the reducer

import sys
import re
import csv

data1=[]

for line in csv.reader(sys.stdin,delimiter='\t'):
    data1.append(line)
 
for data in data1:
    node_type = data[5]
    parent_id = data[6]
    body = data[4]
    id = data[0]
    if node_type == 'answer' or node_type == 'question':
       if parent_id == "\\N":
          parent_id = id # if there is no parent id then set id to be the parent id
       print(parent_id + "\t" + node_type + "\t" + str(len(body)))          


