"""Physics subject module"""

class Physics:
    """Handles physics-related questions and concepts"""
    
    def __init__(self):
        self.concepts = {
            'force': 'Force is a push or pull on an object, measured in Newtons (N).',
            'motion': 'Motion is a change in position of an object over time.',
            'velocity': 'Velocity is the speed of an object in a specific direction.',
            'acceleration': 'Acceleration is the rate of change of velocity over time.',
            'gravity': 'Gravity is the force that pulls objects toward the Earth.',
            'energy': 'Energy is the ability to do work or cause change, measured in Joules (J).'
        }
    
    def answer(self, question):
        """
        Answer physics questions
        
        Args:
            question (str): Physics question
            
        Returns:
            str: Answer to the question
        """
        question_lower = question.lower()
        
        for concept, explanation in self.concepts.items():
            if concept in question_lower:
                return explanation
        
        return "I can help with physics questions about: force, motion, velocity, acceleration, gravity, and energy."
    
    def solve_problem(self, problem_type, **kwargs):
        """
        Solve physics problems
        
        Args:
            problem_type (str): Type of problem to solve
            **kwargs: Problem parameters
            
        Returns:
            str: Solution to the problem
        """
        if problem_type == 'distance':
            # distance = velocity * time
            velocity = kwargs.get('velocity', 0)
            time = kwargs.get('time', 0)
            distance = velocity * time
            return f"Distance = {distance} meters"
        
        return "Problem type not supported yet."
