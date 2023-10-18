from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.

admin.site.register(Publisher)