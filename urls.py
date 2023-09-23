"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from django.urls import include
from . import views
from .upload import views as upload_views


urlpatterns = [
    path(
        'upload/private_upload/', 
        upload_views.private_upload, 
        name='mediacenter__private_upload'
    ),
]