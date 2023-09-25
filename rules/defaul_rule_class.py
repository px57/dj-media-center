
from django.utils import timezone
import os
from mediacenter.rules.stack import RULESTACK

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
    def max_file_size():
        """
            @description: The maximum file size uploaded
        """

    @property
    def upload_to(self, instance, filename):
        """
            @description: The position to upload the file.
        """
        now = timezone.now()
        # TODO: 
        return os.path.join(
            'upload',
            instance.label,
            str(now.year),
            str(now.month),
            str(now.day),
            filename
        )
    
    @property
    def autocrop(self, instance):
        """
            @description: Return the size to autocrop the image.
        """
        return '100x100'

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ EVENT @@@
    
    def event_after_upload(self, request, instance):
        """
            @description: This function is called after the upload.
            TODO: Par defaut qu'est-ce que l'ont doit faire ici ? 
        """
        print ('event_after_upload')

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
    
    def run_autocrop(self):
        """
            @description: Autocrop the image.
        """
        if not self.autocrop:
            return;
        return self.autocrop

RULESTACK.set_rule(DefaultRuleClass())