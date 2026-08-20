"""Main chatbot module"""
from features.calculator import Calculator
from features.grammar import Grammar
from subjects.physics import Physics
from subjects.chemistry import Chemistry
from subjects.biology import Biology
from subjects.government import Government
from subjects.general_questions import GeneralQuestions

class Chatbot:
    """Main chatbot class that coordinates responses"""
    
    def __init__(self):
        self.calculator = Calculator()
        self.grammar = Grammar()
        self.physics = Physics()
        self.chemistry = Chemistry()
        self.biology = Biology()
        self.government = Government()
        self.general_questions = GeneralQuestions()
    
    def get_response(self, user_input):
        """
        Process user input and return appropriate response
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Chatbot's response
        """
        user_input_lower = user_input.lower()
        
        # Check for greetings
        greeting_response = None
        if any(keyword in user_input_lower for keyword in ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening', 'howdy']):
            greeting_response = "Hi! 👋 How can I help you today?"
        
        # Check for calculator queries
        if any(keyword in user_input_lower for keyword in ['calculate', 'math', 'solve', '+', '-', '*', 'x', '/', 'divide', 'multiply', 'square', 'power', '^', 'root', 'sqrt']):
            if greeting_response:
                return greeting_response + "\n" + self.calculator.solve(user_input)
            return self.calculator.solve(user_input)
        
        # Check for grammar queries
        if any(keyword in user_input_lower for keyword in ['grammar', 'spell', 'correct', 'is this correct', 'is this right', 'check this']):
            if greeting_response:
                return greeting_response + "\n" + self.grammar.check(user_input)
            return self.grammar.check(user_input)
        
        # Check for subject-specific queries
        if any(keyword in user_input_lower for keyword in ['physics', 'force', 'motion', 'velocity', 'acceleration', 'gravity', 'energy']):
            if greeting_response:
                return greeting_response + "\n" + self.physics.answer(user_input)
            return self.physics.answer(user_input)
        
        if any(keyword in user_input_lower for keyword in ['chemistry', 'reaction', 'element', 'atom', 'molecule', 'ph', 'oxidation']):
            if greeting_response:
                return greeting_response + "\n" + self.chemistry.answer(user_input)
            return self.chemistry.answer(user_input)
        
        if any(keyword in user_input_lower for keyword in ['biology', 'cell', 'organism', 'dna', 'photosynthesis', 'evolution', 'ecosystem']):
            if greeting_response:
                return greeting_response + "\n" + self.biology.answer(user_input)
            return self.biology.answer(user_input)
        
        if any(keyword in user_input_lower for keyword in ['government', 'politics', 'law', 'democracy', 'constitution', 'rights']):
            if greeting_response:
                return greeting_response + "\n" + self.government.answer(user_input)
            return self.government.answer(user_input)
        
        if any(keyword in user_input_lower for keyword in ['nigeria', 'akure', 'ondo', 'telnet', 'school', 'culture', 'history', 'capital', 'currency', 'president', 'general manager', 'principal', 'vice principal', 'head of', 'staff', 'management', 'jane edet', 'odunayo shittu', 'opeyemi oladehinde', 'tolulope adewumi', 'joseph bello', 'sogo', 'director', 'ariyo']):
            if greeting_response:
                return greeting_response + "\n" + self.general_questions.answer(user_input)
            return self.general_questions.answer(user_input)
        
        # If only greeting, return greeting
        if greeting_response:
            return greeting_response
        
        # Default response
        return "I'm an educational chatbot."
