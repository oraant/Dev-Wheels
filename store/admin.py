from django.contrib import admin
from store.models import TimeSeriesDatabase

# Register your models here.
class TimeSeriesDatabaseAdmin(admin.ModelAdmin):
    list_display = ('id','name','license','intro','grade','desc','up','down','record','version')
    fieldsets = (
        ['Main',{
                'fields':('name','link','license','intro',),
        }],
        ['Descriptions',{
            'classes': ('collapse',), # CSS
            'fields':('grade','desc','imgs','tags',),
        }],
        ['Votes',{
            'classes': ('collapse',), # CSS
            'fields': ('up','down','watch','star','fork',),
        }],
        ['Times',{
            'fields': ('record','version','start','end',),
        }],
        ['Others',{
            'classes': ('collapse',), # CSS
            'fields': ('country','company',),
        }],
    )

# Register your models here.
admin.site.register(TimeSeriesDatabase,TimeSeriesDatabaseAdmin)
