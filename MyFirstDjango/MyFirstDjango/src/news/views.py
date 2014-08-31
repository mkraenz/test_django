from django.shortcuts import render

# Create your views here.

from news.models import Meldung, Kommentar 
from django.http import HttpResponse, Http404
 
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


def meldung_detail(request, meldungs_id): 
    try: 
        m = Meldung.objects.get(id=meldungs_id) 
    except Meldung.DoesNotExist: 
        raise Http404 
 
    zeilen = [ 
        "Titel: '%s' vom %s" % (m.title, m.timestamp), 
        "Text: %s\n" % m.text, 
        "-" * 30 + "", 
        "Kommentare:", 
        ""] 
 
    zeilen += ["%s: %s" % (k.autor, k.text) 
               for k in m.kommentar_set.all()] 
 
    antwort = HttpResponse("\n".join(zeilen)) 
    antwort["Content-Type"] = "text/plain" 
    return antwort