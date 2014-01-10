
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades

def remove_record_with_lowest_score_from_homework():
    print 'remove, report'

    try:
        iter = grades.find().sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
    except:
        print 'Unexpected error:', sys.exc_info()[0]

    sanity = 0
    prevDoc = None
    for doc in iter:
        if prevDoc and (prevDoc['student_id'] != doc['student_id']):
            if prevDoc['type'] == 'homework':
                # delete the document
                grades.remove(prevDoc)
        prevDoc = doc    


        #print doc
        #sanity += 1
        #if (sanity > 10):
        #    break

remove_record_with_lowest_score_from_homework()  
# 696 count
