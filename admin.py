from django.contrib import admin
from .models import FilesModel, FilesPermission

@admin.register(FilesModel)
class FilesModelAdmin(admin.ModelAdmin):    
    pass
    # list_display = ('id', 'profile', 'file_name', 'src', 'md5', 'label')
    # list_filter = ('profile', 'file_name', 'src', 'md5', 'label')
    # search_fields = ('profile', 'file_name', 'src', 'md5', 'label')