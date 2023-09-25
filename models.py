from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.http.serialize.media import serialize_file_fields, serialize_phone_number, serialize_size_video
from kernel.crypt.md5 import md5_file
from django.utils import timezone
import hashlib
import os

def dynamic_upload_to(instance, filename):
    now = timezone.now()
    # TODO: 
    return os.path.join(
        'upload',
        instance.label,
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
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
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


    def set_file_name(self, file_name): 
        """
            @description: 
        """
        real_name = file_name
        extension = file_name.split('.')[-1]
        self.file_name = real_name
        # TODO: Generer le nom du fichier en uuid.
            # image.name = f'{uuid.uuid4().hex}.{extension}'
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

    def serialize(self, request):
        """
            @description:
        """
        return {
            'src': serialize_file_fields(request, self.src),
        }