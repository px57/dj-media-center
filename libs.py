import PIL
from PIL import Image

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
    # TODO: Get the resolution of the pdf, odt etc...