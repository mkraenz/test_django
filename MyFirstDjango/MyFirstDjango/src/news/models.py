
'''
Created on 30.08.2014

@author: proSingularity
'''

from django.db import models

       
# Create your models here.
class Meldung(models.Model):
    title = models.CharField(max_length = 100)
    timestamp = models.DateTimeField()
    text = models.TextField("Meldungstext")
        
    def __unicode__(self): 
        return self.text 
    
    class Admin:
        pass
    
class Kommentar(models.Model):
    
    news = models.ForeignKey(Meldung) 
    autor = models.CharField(max_length=70) 
    text = models.TextField("Text")
    
    def __unicode__(self): 
        return self.text 
    
    class Admin:
        pass
