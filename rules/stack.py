
class RulesStack:
    """
        @description: 
    """

    def __init__(self) -> None:
        """
            @description: 
        """
        self.rules = {

        } 

    def set_rule(self, ruleClass):
        """
            @description: This function sets the rule 
        """
        self.rules[ruleClass.label] = ruleClass

    def get_rule(self, label):
        """
            @description: Get the rule or raise an exception.
        """
        if label in self.rules:
            return self.rules[label]
        
        raise Exception('The rule with the label: ' + label + ' does not exist')


RULESTACK = RulesStack()