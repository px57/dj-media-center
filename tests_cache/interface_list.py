from mediacenter.rules.stack import MEDIACENTER_RULESTACK
from mediacenter.rules.defaul_rule_class import DefaultRuleClass


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [AVATAR-FILE-RULE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class AvatarFileRule(DefaultRuleClass):
    """
        @description: This class is the avatar file rule
    """

    @property
    def label(self):
        return 'avatar'
    
    def event_after_upload(self, request, instance):
        request.profile.avatar = instance
        request.profile.save()
        return super().event_after_upload(request, instance)
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [EXTRACT-FILE-RULE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
 
class ExtractFileRule(DefaultRuleClass):
    """
        @description: This class is the extract file rule
    """

    extracttexttodocument_allow = True

    @property
    def label(self):
        return 'extract_file_rule'

    
    def event_after_upload(self, request, instance):
        request.profile.extract = instance
        request.profile.save()
        return super().event_after_upload(request, instance)
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

MEDIACENTER_RULESTACK.set_rule(AvatarFileRule())

