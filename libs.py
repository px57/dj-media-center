
import PIL
from PIL import Image
import os
from kernel.http.request import generate_fake_request
from kernel.http.response import get_fake_response
import shutil
import magic

def get_mime_type(file_path: str) -> str:
    """
        @description: Get the mime type of the file.
    """
    mime = magic.Magic()
    mime_type = mime.from_file(file_path)
    if mime_type == 'empty':
        mime_type = 'application/octet-stream'
    return mime_type


def mkdir_if_not_exist(path: str):
    """
        @description: Create a directory if not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def copy_file(source_path, destination_path):
    """
        @description: Copy a file from source to destination.
    """
    mkdir_if_not_exist(os.path.dirname(destination_path))
    try:
        # Copy the file from source to destination
        shutil.copy(source_path, destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying file: {str(e)}")

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
        @params.label -> instance label.
        @params.file -> file pathname. 
        @params.dbProfile -> Profile. 
    """
    from  mediacenter.models import FilesModel
    from mediacenter.rules.stack import MEDIACENTER_RULESTACK

    if not os.path.exists(file):
        raise Exception('File not found ' + file)
    
    file_name = get_file_name_tofileSrc(file)
    fileManager = MEDIACENTER_RULESTACK.get_rule(label_interface)
    res = get_fake_response(profile=dbProfile)

    dbFileModel = FilesModel(
        src=file,
        profile=dbProfile,
        label=label_interface,
    )

    fileManager.event_before_copied(res, dbFileModel)
    copy_file(
        file, 
        dbFileModel.src.path
    )
    # dbFileModel.
    dbFileModel.save()
    process_set_file(
        res,
        dbFileModel, 
        get_file_name_tofileSrc(file)
    )
    fileManager.event_after_copied(res, dbFileModel)
    return dbFileModel

def get_file_name_tofileSrc(file: str):
    """
        @description:   
    """
    if not os.path.exists(file):
        raise Exception('File not found ' + file)
    return os.path.basename(file)

def process_set_file(
        res, 
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
    # fileManager.event_

    fileManager.run_autocrop(res, dbFileModel)
    # dbFileModel.update_md5(save=False)
    dbFileModel.update_resolutions(save=False)
    fileManager.run_extracttexttodocument(res, dbFileModel)

def create_attachment_file(
        label_interface: str,
        dbFile: object,
        file_path: str,
        dbProfile: object or None=None
    ):
    """
        @description:
        @params.label_interface -> 
        @params.dbFile -> 
        @params.file_path ->  
    """
    dbRattachedFile = external_set_file(
        label_interface,
        file_path,
        dbProfile=dbProfile
    )
    dbRattachedFile.rattached_file = dbFile 
    dbRattachedFile.save()