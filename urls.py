"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
# from django.urls import include
from mediacenter import views
from mediacenter.upload import views as upload_views


urlpatterns = [
    path(
        'upload/private_upload/', 
        upload_views.private_upload, 
        name='mediacenter__private_upload'
    ),
    # path(
    #     'documents/download/<int:id>/', 
    #      views.download_document, 
    #      name='download_document'),
    path(
        'documents/download/<int:id>/<slug:file_name>.pdf',
        views.download_document,
        name='download_document'
    ),
]