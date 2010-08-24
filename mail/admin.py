from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib import admin
from fodcl.mail.models import Record,StreamWader,Survey

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/textareas.js',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name','email','home_addr','lake_addr')
    search_fields = ('name','email','home_addr','lake_addr')
    
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Survey)
admin.site.register(Record,RecordAdmin)
admin.site.register(StreamWader)
