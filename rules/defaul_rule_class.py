
from django.utils import timezone
import os
from mediacenter.rules.stack import MEDIACENTER_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
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

    def before_extracttexttodocument(self, instance):
        """
            @description: This function is called before the extracttexttodocument.
        """
        pass

    def after_extracttexttodocument(self, instance):
        """
            @description: This function is called after the extracttexttodocument.
        """
        pass

    def run_extracttexttodocument(self, request, instance):
        """
            @description: Extract the text to the document.
        """

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [AUTOCROP] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # @description: Autocrop the image.
    autocrop_allow = False

    def autocrop(self, instance):
        """
            @description: Return the size to autocrop the image.
        """
        return '100x100'

    def event_after_autocrop(self, instance):
        """
            @description: This function is called after the crop.
        """
        pass

    def event_before_autocrop(self, instance):
        """
            @description: This function is called before the crop.
        """
        pass    

    def run_autocrop(self, request, instance):
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
    #     cmd = """
    #         convert -define jpeg:size={{IMG_WIDTH}}x{{IMG_HEIGHT}} {{img_src}}  -thumbnail 428x428^ \
    #                 -gravity center -extent 428x428 {{img_src}}
    #     """
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
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [LABEL] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    @property
    def label(self):
        """
            @description: The label of the rule
        """
        return 'default'

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
    def before_copied(self, instance):
        """
            @description: This function is called before copied.
        """
        pass
    
    def after_copied(self, instance):
        """
            @description: This function is called after copied.
        """
        pass
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


MEDIACENTER_RULESTACK.set_rule(DefaultRuleClass())