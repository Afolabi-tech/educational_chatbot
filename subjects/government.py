"""Government subject module"""

class Government:
    """Handles government and civics-related questions"""
    
    def __init__(self):
        self.concepts = {
            'democracy': 'Democracy is a system of government where power rests with the people.',
            'constitution': 'A constitution is the fundamental set of rules governing a state or organization.',
            'law': 'A law is a rule enforced by the government that members of society must follow.',
            'government': 'Government is the system or group of people that runs a country or state.',
            'politics': 'Politics is the activity of participating in decisions about the governance of a country.',
            'rights': 'Rights are entitlements or permissions that are guaranteed to individuals.'
        }
    
    def answer(self, question):
        """
        Answer government and civics questions
        
        Args:
            question (str): Government question
            
        Returns:
            str: Answer to the question
        """
        question_lower = question.lower()
        
        for concept, explanation in self.concepts.items():
            if concept in question_lower:
                return explanation
        
        return "I can help with government questions about: democracy, constitution, law, politics, and rights."
    
    def explain_branch(self, branch_name):
        """
        Explain branches of government
        
        Args:
            branch_name (str): Name of the government branch
            
        Returns:
            str: Explanation of the branch
        """
        branches = {
            'executive': 'The executive branch enforces laws and is headed by the President.',
            'legislative': 'The legislative branch makes laws and consists of Congress.',
            'judicial': 'The judicial branch interprets laws and is headed by the Supreme Court.'
        }
        
        return branches.get(branch_name.lower(), f"Branch {branch_name} not found.")
