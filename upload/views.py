from kernel.http import Response
from profiles.decorators import load_profile
from mediacenter.models import FilesModel
import uuid

@load_profile
def private_upload(request):
    """
        @description:
    """
    res = Response()
    file = request.FILES.get('file', None)
    label = request.POST.get('label', None)

    dbFileModel = FilesModel(
        src=file,
        profile=request.profile,
        label=label,
    )
    dbFileModel.set_file_name(file.name)
    dbFileModel.update_disk_size(save=False)
    # dbFileModel.update_md5(save=False)
    dbFileModel.save()

    # compressAvatar(request, dbUploaded, image)

    # res.status = 'done'
    # res.url = settings.ADRESS_HOST + settings.MEDIA_URL + dbUploaded.src.name
    # res.thumbUrl = settings.ADRESS_HOST + settings.MEDIA_URL + dbUploaded.src.name
    # res.name = image.name
    # for key in request.GET:
    #     setattr(res, key, request.GET.get(key))
    return res.success()
