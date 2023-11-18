from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from mediacenter.models import FilesModel

# # @login_required
# def download_document(request, id):
#     try:
#         document = FilesModel.objects.get(id=id)
#         response = FileResponse(document.src, content_type='application/pdf')
#         response['Content-Disposition'] = f'inline; filename="{document.file_name}.pdf"'
#         return response
#     except FilesModel.DoesNotExist:
#         raise Http404("Document does not exist")
    

def download_document(request, id, file_name):
    try:
        document = FilesModel.objects.get(id=id)
        # Optionally, you could also check if the file_name matches the document's file name
        response = FileResponse(document.src, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{file_name}.pdf"'
        return response
    except FilesModel.DoesNotExist:
        raise Http404("Document does not exist")
        

    # def download_document(request, id):
    # try:
    #     document = FilesModel.objects.get(id=id)
    #     response = FileResponse(document.src.open(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline; filename="{}"'.format(document.file_name)
    #     return response
    # except FilesModel.DoesNotExist:
    #     raise Http404("Document does not exist")