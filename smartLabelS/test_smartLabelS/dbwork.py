'''
Created on Apr 4, 2014

@author: al
'''
from django.db.models.query import RawQuerySet 

class dbwork(object):
    '''
    classdocs
    '''
    def saekja(self):
        return RawQuerySet.using("rfid").raw_query("SELECT * FROM shipment")


    def __init__(self):
        '''
        Constructor
        '''
        