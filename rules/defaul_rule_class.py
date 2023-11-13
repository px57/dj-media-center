
from django.utils import timezone
import os
from mediacenter.rules.stack import MEDIACENTER_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
# from mediacenter.
import PIL

class DefaultRuleClass(InterfaceManager):
    """
        @description: The default rule class. 
    """

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [EXTRACT-DOCUMENT] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -> Extraire le texte du document. 
    extracttexttodocument_allow = False

    # -> The liste of mime type accepted, to extract the text.
    extracttexttodocument_mime_type_accepted = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.ms-excel',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-powerpoint',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    ]

    def before_extracttexttodocument(self, res, instance):
        """
            @description: This function is called before the extracttexttodocument.
        """
        pass

    def after_extracttexttodocument(self, res, instance):
        """
            @description: This function is called after the extracttexttodocument.
        """
        pass

    def run_extracttexttodocument(self, res, instance):
        """
            @description: Extract the text to the document.

        """
        # TODO: Extract the text to the document.

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [AUTOCROP] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # @description: Autocrop the image.
    autocrop_allow = False

    def autocrop(self, instance):
        """
            @description: Return the size to autocrop the image.
        """
        return '100x100'

    def event_after_autocrop(self, res, instance):
        """
            @description: This function is called after the crop.
        """
        pass

    def event_before_autocrop(self, res, instance):
        """
            @description: This function is called before the crop.
        """
        pass    

    def run_autocrop(self, res, instance):
        """
            @description: Autocrop the image.
        """

        if not self.autocrop(instance):
            return; 
        if instance.autocropped_size is not None:
            return; 
        if instance.is_image() is False:
            return; 

        instance.autocropped_size = self.autocrop(instance)

        # cmd = """
        #   convert -define jpeg:size={{IMG_WIDTH}}x{{IMG_HEIGHT}} {{img_src}}  -thumbnail 428x428^ \
        #   -gravity center -extent 428x428 {{img_src}}
        # """
        # cmd = cmd.replace('{{IMG_WIDTH}}', str(width))
        # cmd = cmd.replace('{{IMG_HEIGHT}}', str(height))
        # cmd = cmd.replace('{{img_src}}', path)
        # os.system(cmd)

        instance.update_disk_size(save=False)
        # TODO: Uncomment this line.
        # instance.update_md5(save=False)
        instance.update_resolutions(save=False)
        instance.save()

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [CROP] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -> Crop the image.
    crop_allow = False

    def event_after_crop(self, instance):
        """
            @description: This function is called after the crop.
        """
        pass

    def event_before_crop(self, instance):
        """
            @description: This function is called before the crop.
        """
        pass

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [DEFAULT INTERFACE NAME] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
    @property
    def label(self):
        return 'defaultruleclass'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [MIME-TYPE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    @property
    def type_mime_accepted():
        """
            @description:
            @return [
                
            ]  
            @return '*' -> All file accepted
        """
        return '*'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [MAX-FILE-SIZE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    @property
    def max_file_size(self):
        """
            @description: The maximum file size uploaded
        """
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [UPLOAD-TO] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    @property
    def upload_to(self, instance, filename):
        """
            @description: The position to upload the file.
        """
        now = timezone.now()
        return os.path.join(
            'upload',
            instance.label,
            str(now.year),
            str(now.month),
            str(now.day),
            filename
        )
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [EVENT] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def event_after_upload(self, request, instance):
        """
            @description: This function is called after the upload.
        """
        pass

    def event_before_upload(self, request, instance):
        """
            @description: This function is called before the upload.
        """
        pass


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [CROP] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def event_before_copied(self, res, dbFileModel):
        """
            @description: This function is called before copied.
        """
        pass
    
    def event_after_copied(self, res, dbFileModel):
        """
            @description: This function is called after copied.
        """
        pass
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [CONVERT TO MP4] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    convert_video_to_mp4 = False
    convert_video_to_mp4_ffmpeg_config = {
        'codec': 'libx264',
        'bitrate': '500k',
        'audio_codec': 'aac',
        'audio_bitrate': '128k',
        'audio_channels': '2',
    }


    def event_before_convert_video_to_mp4(self, instance):
        """
            @description: This function is called before the convertion.
        """
        pass

    def event_after_convert_video_to_mp4(self, instance):
        """
            @description: This function is called after the convertion.
        """
        pass

    def run_convert_video_to_mp4(self, instance):
        """
            @description: Convert the video to mp4.
        """
        pass
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [STREAMING] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    streaming = False
    stream_services = [
        'youtube',
        'vimeo',
        {
            'label': 'dailymotion',
            'url': 'https://www.dailymotion.com/embed/video/{{VIDEO_ID}}'
        },
    ]

    def event_before_streaming_send(self, instance):
        """
            @description: This function is called before the streaming.
        """
        pass

MEDIACENTER_RULESTACK.set_rule(DefaultRuleClass())