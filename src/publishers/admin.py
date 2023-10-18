from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.

class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'created')
    
    
    
class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PublisherResource


admin.site.register(Publisher, PublisherAdmin)