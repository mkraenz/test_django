from django.contrib import admin

# Register your models here.

from news.models import Meldung, Kommentar

class PageAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Meldung, PageAdmin )
admin.site.register( Kommentar, PageAdmin)