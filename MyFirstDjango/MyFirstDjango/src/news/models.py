
'''
Created on 30.08.2014

@author: proSingularity
'''

from django.db import models

       
# Create your models here.

class Meldung(models.Model):
    '''
    classdocs
    '''
    title = models.CharField(max_length = 100)
    timestamp = models.DateTimeField()
    text = models.TextField("Meldungstext")


    def __init__(self, params):
        '''
        Constructor
        '''
        models.Model(self, params)
        
        
class Kommentar(models.Model):
    '''
    classdocs
    '''
    
    news = models.ForeignKey(Meldung) 
    autor = models.CharField(max_length=70) 
    text = models.TextField("Text")

    def __init__(self, params):
        '''
        Constructor
        '''
        models.Model(self, params)
        
 