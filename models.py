from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict

from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.http.serialize.media import serialize_file_fields, serialize_phone_number, serialize_size_video
from kernel.crypt.md5 import md5_file
from mediacenter.libs import get_resolution_by_image, get_resolution_by_video, get_resolution_by_document, get_mime_type

import mimetypes
import magic
import hashlib
import os

def dynamic_upload_to(instance, filename):
    now = timezone.now()
    # TODO: Gerer le dynamique upload_to au sein d'une autre elements.
    return os.path.join(
        'upload',
        str(instance.label),
        str(now.year),
        str(now.month),
        str(now.day),
        filename
    )

class FilesPermission(BaseMetadataModel):
    """
        @description:
    """
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    file = models.ForeignKey(
        'FilesModel',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    

class FilesModel(BaseMetadataModel):
    """
        @description: 
    """
    @property
    def file_path(self):
        """
            @description: 
        """
        file_path = self.src.path
        return file_path

    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    rattached_file = models.ForeignKey(
        'mediacenter.FilesModel',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    file_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    
    src = models.FileField(
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
        default=None
    )

    md5 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    label = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    disk_size = models.IntegerField(
        null=True,
        blank=True,
        default=None
    )

    autocropped_size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    mime_type = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None
    )

    resolutions = models.JSONField(
        null=True,
        blank=True,
        default={
            'width': None,
            'height': None,
        }
    )
 
    def set_file_name(self, file_name): 
        """
            @description: 
        """
        real_name = file_name
        extension = file_name.split('.')[-1]
        self.file_name = real_name
        self.file_name = file_name

    def update_disk_size(self, save=True):
        """
            @description: 
        """
        self.disk_size = self.src.size
        self.run_save(save)

    def update_md5(self, save=True):
        """
            @description: Get the md5 of the file 
        """
        self.md5 = md5_file(self.src.path)
        self.run_save(save)

    def update_mime_type(self, save=True):
        """
            @description:
        """
        try: 
            self.mime_type = get_mime_type(self.src.file)
        except: 
            self.mime_type = 'application/octet-stream'
        self.run_save(save)

    def update_resolutions(self, save=True):
        """
            @description: 
        """
        if self.is_image():
            self.resolutions = get_resolution_by_image(self)
        elif self.is_video():
            self.resolutions = get_resolution_by_video(self)
        elif self.is_document():
            self.resolutions = get_resolution_by_document(self)
        else: 
            self.resolutions = None
        self.run_save(save)

    def is_image(self):
        """
            @description: 
        """
        return self.mime_type.startswith('image')
    
    def is_video(self):
        """
            @description:
        """
        return self.mime_type.startswith('video')
    
    def is_document(self):
        """
            @description: 
        """
        return self.mime_type.startswith('document')

    def serialize(self, request):
        """
            @description:
        """
        serialize = model_to_dict(self)
        serialize['src'] = serialize_file_fields(request, self.src)
        return serialize