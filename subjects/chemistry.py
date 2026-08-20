"""Chemistry subject module"""

class Chemistry:
    """Handles chemistry-related questions and concepts"""
    
    def __init__(self):
        self.concepts = {
            'atom': 'An atom is the smallest unit of matter that retains all the properties of an element.',
            'molecule': 'A molecule is a group of atoms bonded together.',
            'element': 'An element is a substance made of only one type of atom.',
            'reaction': 'A chemical reaction is a process where substances are transformed into different substances.',
            'pH': 'pH is a measure of how acidic or basic a substance is, on a scale of 0-14.',
            'oxidation': 'Oxidation is the loss of electrons by an atom during a chemical reaction.'
        }
    
    def answer(self, question):
        """
        Answer chemistry questions
        
        Args:
            question (str): Chemistry question
            
        Returns:
            str: Answer to the question
        """
        question_lower = question.lower()
        
        for concept, explanation in self.concepts.items():
            if concept in question_lower:
                return explanation
        
        return "I can help with chemistry questions about: atoms, molecules, elements, reactions, pH, and oxidation."
    
    def get_element_info(self, element_name):
        """
        Get information about chemical elements
        
        Args:
            element_name (str): Name of the element
            
        Returns:
            str: Information about the element
        """
        elements = {
            'hydrogen': 'H - Atomic number 1, lightest element',
            'oxygen': 'O - Atomic number 8, essential for combustion',
            'carbon': 'C - Atomic number 6, basis of organic chemistry'
        }
        
        return elements.get(element_name.lower(), f"Element {element_name} not found in database.")
