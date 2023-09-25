
from django.utils import timezone
import os
from mediacenter.rules.stack import RULESTACK
import PIL

class DefaultRuleClass(object):
    """
        @description: The default rule class. 
    """

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ PROPERTY @@@
    # @description: Autocrop the image.
    autocrop = False

    @property
    def type_mime_accepted():
        """
            @description:
            @return [
                
            ]  
            @return '*' -> All file accepted
        """
        return '*'

    @property
    def label(self):
        """
            @description: The label of the rule
        """
        return 'default'

    @property
    def max_file_size(self):
        """
            @description: The maximum file size uploaded
        """

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
    
    def autocrop(self, instance):
        """
            @description: Return the size to autocrop the image.
        """
        return '100x100'

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ EVENT @@@
    
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

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ FUNCTION @@@
    
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
        # instance.save()
        image = PIL.Image.open(instance.src.path)
        print (instance.autocropped_size)



RULESTACK.set_rule(DefaultRuleClass())