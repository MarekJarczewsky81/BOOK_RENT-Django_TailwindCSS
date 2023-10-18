from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.

class PublisherResource(resources.ModelResource):
    created = Field()
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'created')
        
    def dehydrate_created(self, obj):
        return obj.created.strftime("%d/%m/%y")
        
    
    
    
class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PublisherResource


admin.site.register(Publisher, PublisherAdmin)