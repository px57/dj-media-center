
import PIL
from PIL import Image
import os
from kernel.http.request import generate_fake_request

# from .models import FilesModel
# from profiles.models import Profile

def get_resolution_by_image(instance):
    """
        @description: 
    """
    img = PIL.Image.open(instance.src)
    return {
        'width': img.width,
        'heigth': img.height,
    }

def get_resolution_by_video(instance):
    """
        @description:
    """
    pass
    # TODO: Get the resolution of the video.

def get_resolution_by_document(instance):
    """
        @description:
    """
    pass
    # TODO: Get the resolution of the pdf, odt etc...\


def external_set_file(
        label_interface: str,
        file: str, 
        dbProfile=None,
    ):
    """
        @description: Set the file, with the os systeme. 
    """
    from  mediacenter.models import FilesModel
    from mediacenter.rules.stack import MEDIACENTER_RULESTACK

    if not os.path.exists(file):
        raise Exception('File not found ' + file)
    
    file_name = get_file_name_tofileSrc(file)
    fileManager = MEDIACENTER_RULESTACK.get_rule(label_interface)
    request = generate_fake_request(profile=dbProfile)
    # TODO: Deplacer le fichiers vers ca destinations final.

    # print (fileManager.upload_to(fileManager, file_name))

    dbFileModel = FilesModel(
        src=file,
        profile=dbProfile,
        label=label_interface,
    )
    # process_set_file(
    #     request, 
    #     dbFileModel, 
    #     get_file_name_tofileSrc(file)
    # )


def get_file_name_tofileSrc(file: str):
    """
        @description:   
    """
    if not os.path.exists(file):
        raise Exception('File not found ' + file)
    return os.path.basename(file)

def process_set_file(
        request, 
        dbFileModel, 
        file_name: str=''):
    """
        @description: 
    """
    from mediacenter.rules.stack import MEDIACENTER_RULESTACK
    fileManager = MEDIACENTER_RULESTACK.get_rule(dbFileModel.label)

    dbFileModel.set_file_name(file_name)
    dbFileModel.update_disk_size(save=False)
    dbFileModel.update_mime_type(save=False)
    dbFileModel.save()

    fileManager.run_autocrop(request, dbFileModel)
    # dbFileModel.update_md5(save=False)
    dbFileModel.update_resolutions(save=False)
