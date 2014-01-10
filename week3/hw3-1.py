'''
Created on Sep 28, 2013

@author: ray

@summary: Remove the lowest homework score for each student

'''

import pymongo
import sys
from pprint import pprint
from pymongo import MongoClient

# establish a connection to the database
client = MongoClient("mongodb://localhost")

# get a handle to the school database
db = client.school
students = db.students

try:
    docs = students.find()
    for doc in docs:
        min_score = None       # assume score > 0
        for score in doc['scores']:
            if score['type'] != 'homework':
                continue
            if not min_score or float(min_score['score']) > float(score['score']):
                min_score = score
        
        # Remove the lowest homework score        
        if min_score:
            #print('_id={0} score={1}'.format(doc['_id'], min_score))
            students.update({'_id':doc['_id']}, {'$pull':{'scores':min_score}})
            
except:
    print 'Unexpected error:', sys.exc_info()[0]
