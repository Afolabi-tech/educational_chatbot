"""Calculator feature for solving math problems"""
import re
import math

class Calculator:
    """Handles mathematical calculations and problems"""
    
    def solve(self, expression):
        """
        Solve mathematical expressions
        
        Args:
            expression (str): Math expression to solve
            
        Returns:
            str: Result of calculation
        """
        try:
            # Remove common text patterns
            expr = expression.lower().replace('calculate ', '').replace('solve ', '').replace('what is ', '').strip()
            
            # Convert text patterns to mathematical operators
            # "square root of X" or "root X" -> math.sqrt(X)
            expr = re.sub(r'square root of\s+([\d.]+)', r'math.sqrt(\1)', expr)
            expr = re.sub(r'sqrt of\s+([\d.]+)', r'math.sqrt(\1)', expr)
            expr = re.sub(r'(?:^|\s)root\s+([\d.]+)', r' math.sqrt(\1)', expr)
            
            # "square of X" or "X squared" -> X**2
            expr = re.sub(r'square of\s+([\d.]+)', r'\1**2', expr)
            expr = re.sub(r'([\d.]+)\s+squared', r'\1**2', expr)
            
            # "X raised to power Y" or "X to power Y" -> X**Y
            expr = re.sub(r'([\d.]+)\s+raised\s+to\s+(?:the\s+)?power\s+([\d.]+)', r'\1**\2', expr)
            expr = re.sub(r'([\d.]+)\s+to\s+(?:the\s+)?power\s+([\d.]+)', r'\1**\2', expr)
            
            # Replace text operators with symbols
            expr = expr.replace('times', '*').replace('multiply', '*').replace('divided by', '/')
            expr = expr.replace('divide', '/').replace('plus', '+').replace('minus', '-')
            
            # Replace 'x' with '*' for multiplication (but not in 'math')
            expr = expr.replace(' x ', ' * ').replace('x', '*')
            
            # Remove common text words that don't affect calculation
            expr = expr.replace('the answer is', '').replace('equals', '=')
            
            # Only keep valid expression characters: digits, operators, parentheses, decimal points, and letters (for math functions)
            expr = re.sub(r'[^\d+\-*/().\s\w]', '', expr)
            
            # Evaluate the expression with math.sqrt available
            result = eval(expr, {"__builtins__": {}, "math": math}, {})
            return f"The answer is: {result}"
        except Exception as e:
            return f"This is an Educational Chatbot: I couldn't solve that expression. Please use basic math operators like +, -, *, / or phrases like 'times', 'divided by', 'plus', 'minus', 'raised to power'."
    
    def explain_concept(self, concept):
        """
        Explain mathematical concepts
        
        Args:
            concept (str): Mathematical concept to explain
            
        Returns:
            str: Explanation of the concept
        """
        concepts = {
            'addition': 'Addition is combining two or more numbers together.',
            'subtraction': 'Subtraction is taking away one number from another.',
            'multiplication': 'Multiplication is repeated addition of a number.',
            'division': 'Division is splitting a number into equal parts.'
        }
        
        return concepts.get(concept.lower(), f"I don't have an explanation for {concept}")
