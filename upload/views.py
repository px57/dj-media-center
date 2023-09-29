from kernel.http import Response
from profiles.decorators import load_profile
from mediacenter.models import FilesModel
from mediacenter.rules.stack import RULESTACK
import uuid

@load_profile
def private_upload(request):
    """
        @description:
    """
    res = Response()
    file = request.FILES.get('file', None)
    label = request.POST.get('label', None)
    fileManager = RULESTACK.get_rule(label)

    dbFileModel = FilesModel(
        src=file,
        profile=request.profile,
        label=label,
    )
    fileManager.event_before_upload(request, dbFileModel)
    dbFileModel.set_file_name(file.name)
    dbFileModel.update_disk_size(save=False)
    dbFileModel.update_mime_type(save=False)
    dbFileModel.save()

        # TODO: uncomment this line.
    fileManager.run_autocrop(request, dbFileModel)
    # dbFileModel.update_md5(save=False)
    dbFileModel.update_resolutions(save=False)


    fileManager.event_after_upload(request, dbFileModel)
    
    res.file = dbFileModel.serialize(request)
    return res.success()
