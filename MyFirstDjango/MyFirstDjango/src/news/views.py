from django.shortcuts import render

# Create your views here.

from news.models import Meldung, Kommentar 
from django.http import HttpResponse 
 
def meldungen(request): 
    zeilen = [] 
    for m in Meldung.objects.all(): 
        zeilen.append("Titel: '%s' vom %s" % (m.title, 
                                              m.timestamp)) 
        zeilen.append("Text: %s" % m.text) 
        zeilen.append("") 
        zeilen.append("-" * 30) 
        zeilen.append("") 
 
    antwort = HttpResponse("\n".join(zeilen)) 
    antwort["Content-Type"] = "text/plain" 
    return antwort