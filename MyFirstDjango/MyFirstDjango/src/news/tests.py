from django.test import TestCase

# Create your tests here.
from news.models import Meldung, Kommentar
from datetime import datetime
def create_test_data():
    
    m = Meldung(title="Meldung 1", timestamp=datetime.now(), text="This is the text of Meldung 1.")
    m.save()
    
    m2 = Meldung(title="Meldung 2", timestamp=datetime.now(), text="This is the text of Meldung 2.")
    m2.save()
    k1 = m2.kommentar_set.create(autor="Peter", text="Super!")
    k2 = m2.kommentar_set.create(autor="Jens", text="Klasse!") 
    m2.save()