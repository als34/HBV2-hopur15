'''
Created on Apr 4, 2014

@author: al
'''
#from django.db.models.query import RawQuerySet 
from django.db import connection

class dbwork(object):
    '''
    classdocs
    '''
    def saekja(self):
        self.cursor.execute("SELECT * FROM test_smartLabelS_shipmentmonitor;")
        data = self.cursor.fetchall()
        return str(data)


    def __init__(self):
        '''
        Constructor
        '''
        self.cursor = connection.cursor()
        