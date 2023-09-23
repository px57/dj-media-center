"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'private_upload/',
        views.private_upload,
        name='mediacenter__private_upload'
    ),
]