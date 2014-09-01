
# Create your views here.

from django.shortcuts import render, render_to_response, get_object_or_404
from news.models import Meldung, Kommentar 
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader 

def meldungen(request): 
    ''' version 3'''
    '''
    return render_to_response("news/meldungen.html", 
        {"meldungen" : Meldung.objects.all()}) 
    '''
    
    ''' first example '''
    '''
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
    '''
    
    ''' newer example '''
    
    template = loader.get_template("news/meldungen.html")
    context = RequestContext(request, {"meldungen" : Meldung.objects.all()})
    
    return HttpResponse(template.render(context))
    
    
    

def meldung_detail(request, meldungs_id): 
    meldung = get_object_or_404(Meldung, id=meldungs_id) 
    
    if "kommentar_speichern" in request.GET: 
        name = request.POST.get("besuchername", "") 
        text = request.POST.get("kommentartext", "") 
 
        if name and text: 
            kommentar = meldung.kommentar_set.create( 
                autor=name, text=text) 
            kommentar.save() 
            return HttpResponseRedirect(".") 
 
        else: 
            return render_to_response("news/meldung_detail.html", 
                {"meldung" : meldung, 
                 "fehler": "Sie m&uuml;ssen Ihren Namen und einen Kommentar angeben.", 
                 "besuchername" : name, "kommentartext" : text}) 
    
    
    template = loader.get_template("news/meldung_detail.html")
    context = RequestContext(request, {"meldung" : get_object_or_404(Meldung, id=meldungs_id)})
    
    return HttpResponse(template.render(context))
    
    ''' first example'''
    '''
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
    '''