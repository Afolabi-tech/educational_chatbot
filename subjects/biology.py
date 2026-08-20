"""Biology subject module"""

class Biology:
    """Handles biology-related questions and concepts"""
    
    def __init__(self):
        self.concepts = {
            'cell': 'A cell is the basic unit of life. All living organisms are made of cells.',
            'organism': 'An organism is a living thing that can function independently.',
            'dna': 'DNA (Deoxyribonucleic Acid) is a molecule that carries genetic instructions for life.',
            'photosynthesis': 'Photosynthesis is the process by which plants convert sunlight into chemical energy.',
            'evolution': 'Evolution is the process of change and adaptation in living organisms over time.',
            'ecosystem': 'An ecosystem is a community of organisms and their physical environment.'
        }
    
    def answer(self, question):
        """
        Answer biology questions
        
        Args:
            question (str): Biology question
            
        Returns:
            str: Answer to the question
        """
        question_lower = question.lower()
        
        for concept, explanation in self.concepts.items():
            if concept in question_lower:
                return explanation
        
        return "I can help with biology questions about: cells, organisms, DNA, photosynthesis, evolution, and ecosystems."
    
    def explain_system(self, system_name):
        """
        Explain biological systems
        
        Args:
            system_name (str): Name of the biological system
            
        Returns:
            str: Explanation of the system
        """
        systems = {
            'nervous': 'The nervous system controls all body functions and processes information.',
            'circulatory': 'The circulatory system transports oxygen and nutrients throughout the body.',
            'respiratory': 'The respiratory system takes in oxygen and releases carbon dioxide.'
        }
        
        return systems.get(system_name.lower(), f"System {system_name} not found.")
