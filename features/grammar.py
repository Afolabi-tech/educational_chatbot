"""Grammar checking feature"""

class Grammar:
    """Handles grammar checking and correction"""
    
    def __init__(self):
        # Common spelling errors and corrections
        self.spelling_errors = {
            'sho': 'should',
            'teh': 'the',
            'thier': 'their',
            'your': 'you\'re (if you mean "you are")',
            'dont': 'don\'t',
            'cant': 'can\'t',
            'wont': 'won\'t',
            'recieve': 'receive',
            'occured': 'occurred',
            'seperate': 'separate',
            'definately': 'definitely',
            'accomodate': 'accommodate',
            'wich': 'which',
            'realy': 'really',
            'wich': 'which',
            'becuase': 'because',
            'their': 'there (in some contexts)'
        }
        
        # Subject-verb agreement rules
        self.singular_verbs = ['is', 'has', 'goes', 'runs', 'walks', 'talks', 'sleeps', 'eats', 'does', 'was']
        self.plural_verbs = ['are', 'have', 'go', 'run', 'walk', 'talk', 'sleep', 'eat', 'do', 'were']
        self.singular_pronouns = ['he', 'she', 'it', 'this', 'that', 'i']
        self.plural_pronouns = ['we', 'they', 'these', 'those', 'you']
        
        # Articles (a/an)
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        
        # Common contractions
        self.contractions = {
            'dont': 'don\'t',
            'cant': 'can\'t',
            'wont': 'won\'t',
            'shouldnt': 'shouldn\'t',
            'wouldnt': 'wouldn\'t',
            'didnt': 'didn\'t',
            'isnt': 'isn\'t',
            'arent': 'aren\'t'
        }
    
    def check(self, text):
        """
        Check grammar of given text with detailed feedback and corrections
        
        Args:
            text (str): Text to check
            
        Returns:
            str: Grammar check result with suggestions and corrections
        """
        # Remove common question prefixes
        prefixes = [
            'is this correct:',
            'is this correct',
            'check this:',
            'check this',
            'check grammar:',
            'check grammar',
            'correct this:',
            'correct this',
            'is the grammar correct:',
            'is the grammar correct'
        ]
        
        text_lower = text.lower()
        for prefix in prefixes:
            if text_lower.startswith(prefix):
                text = text[len(prefix):].strip()
                break
        
        issues = []
        text_lower = text.lower()
        words = text_lower.split()
        corrected_words = words.copy()
        
        # Check for spelling errors
        for i, word in enumerate(words):
            clean_word = word.strip('.,!?;:')
            punctuation = ''.join(c for c in word if c in '.,!?;:')
            
            if clean_word in self.spelling_errors:
                issues.append(f"Spelling: '{clean_word}' → '{self.spelling_errors[clean_word]}'")
                corrected_words[i] = self.spelling_errors[clean_word] + punctuation
            elif clean_word in self.contractions:
                issues.append(f"Contraction: '{clean_word}' should be '{self.contractions[clean_word]}'")
                corrected_words[i] = self.contractions[clean_word] + punctuation
        
        # Check for subject-verb agreement
        for i in range(len(words) - 1):
            current_word = words[i].strip('.,!?;:').lower()
            next_word = words[i + 1].strip('.,!?;:').lower()
            next_word_clean = next_word
            next_word_punctuation = ''.join(c for c in words[i + 1] if c in '.,!?;:')
            
            # If current word is a singular pronoun, next word should be singular verb
            if current_word in self.singular_pronouns and next_word in self.plural_verbs:
                singular_form = self._get_singular_form(next_word)
                issues.append(f"Subject-verb agreement: '{current_word}' needs '{singular_form}', not '{next_word}'")
                corrected_words[i + 1] = singular_form + next_word_punctuation
            
            # If current word is a plural pronoun, next word should be plural verb
            if current_word in self.plural_pronouns and next_word in self.singular_verbs:
                plural_form = self._get_plural_form(next_word)
                issues.append(f"Subject-verb agreement: '{current_word}' needs '{plural_form}', not '{next_word}'")
                corrected_words[i + 1] = plural_form + next_word_punctuation
        
        # Check article usage (a vs an)
        for i in range(len(words) - 1):
            word_lower = words[i].strip('.,!?;:').lower()
            next_word = words[i + 1].strip('.,!?;:').lower()
            
            if word_lower == 'a':
                if next_word and next_word[0] in self.vowels:
                    issues.append(f"Article: Use 'an' before '{next_word}', not 'a'")
                    corrected_words[i] = 'an'
            elif word_lower == 'an':
                if next_word and next_word[0] not in self.vowels:
                    issues.append(f"Article: Use 'a' before '{next_word}', not 'an'")
                    corrected_words[i] = 'a'
        
        # Check for formatting issues and fix them
        if text.endswith(','):
            issues.append("Punctuation: Sentence ends with a comma, use a period instead")
        
        if '  ' in text:
            issues.append("Spacing: Multiple spaces detected")
        
        if text and text[0].islower():
            issues.append("Capitalization: Sentence should start with a capital letter")
        
        # Check for missing punctuation
        needs_punctuation = False
        if text and text[-1] not in '.!?,;:-–—':
            issues.append("Punctuation: Sentence should end with proper punctuation")
            needs_punctuation = True
        
        if issues:
            # Build corrected sentence
            corrected_text = ' '.join(corrected_words)
            # Fix spacing
            while '  ' in corrected_text:
                corrected_text = corrected_text.replace('  ', ' ')
            # Capitalize first letter
            if corrected_text:
                corrected_text = corrected_text[0].upper() + corrected_text[1:]
            # Add punctuation if needed
            if needs_punctuation and corrected_text[-1] not in '.!?,;:-–—':
                corrected_text += '.'
            
            return f"Incorrect.\nIssues found: {' | '.join(issues)}\n\n\nCorrect: {corrected_text}"
        return "Grammar looks good!"
    
    def _get_singular_form(self, plural_verb):
        """Convert plural verb to singular"""
        mapping = {
            'are': 'is',
            'have': 'has',
            'go': 'goes',
            'run': 'runs',
            'walk': 'walks',
            'talk': 'talks',
            'sleep': 'sleeps',
            'eat': 'eats',
            'do': 'does',
            'were': 'was'
        }
        return mapping.get(plural_verb, plural_verb + 's')
    
    def _get_plural_form(self, singular_verb):
        """Convert singular verb to plural"""
        mapping = {
            'is': 'are',
            'has': 'have',
            'goes': 'go',
            'runs': 'run',
            'walks': 'walk',
            'talks': 'talk',
            'sleeps': 'sleep',
            'eats': 'eat',
            'does': 'do',
            'was': 'were'
        }
        return mapping.get(singular_verb, singular_verb)
    
    def correct(self, text):
        """
        Attempt to correct grammatical errors
        
        Args:
            text (str): Text to correct
            
        Returns:
            str: Corrected text with explanation
        """
        corrected = text.strip()
        changes = []
        words = corrected.split()
        
        # Capitalize first letter
        if corrected:
            corrected = corrected[0].upper() + corrected[1:]
        
        # Fix common spelling errors
        for i, word in enumerate(words):
            clean_word = word.strip('.,!?;:')
            punctuation = ''.join(c for c in word if c in '.,!?;:')
            
            if clean_word.lower() in self.spelling_errors:
                correction = self.spelling_errors[clean_word.lower()]
                words[i] = correction + punctuation
                changes.append(f"'{clean_word}' → '{correction}'")
            elif clean_word.lower() in self.contractions:
                correction = self.contractions[clean_word.lower()]
                words[i] = correction + punctuation
                changes.append(f"'{clean_word}' → '{correction}'")
        
        corrected = ' '.join(words)
        
        # Remove multiple spaces
        while '  ' in corrected:
            corrected = corrected.replace('  ', ' ')
        
        # Fix ending punctuation
        if corrected and corrected[-1] not in '.!?,;:':
            corrected += '.'
        
        if changes:
            return f"Corrected: {corrected}\nChanges: {', '.join(changes)}"
        return f"Corrected: {corrected}"
    
    def explain_concept(self, concept):
        """
        Explain grammatical concepts
        
        Args:
            concept (str): Grammatical concept to explain
            
        Returns:
            str: Explanation of the concept
        """
        concepts = {
            'subject-verb agreement': 'The verb must match the subject in number. Singular subjects use singular verbs (he/she/it goes) and plural subjects use plural verbs (they go).',
            'article': 'Articles (a, an, the) are used before nouns. Use "an" before vowel sounds and "a" before consonant sounds.',
            'contraction': 'A contraction is a shortened form of a word or phrase, using an apostrophe. Example: "do not" → "don\'t"',
            'capitalization': 'The first letter of a sentence should be capitalized.',
            'punctuation': 'End sentences with proper punctuation marks: period (.), question mark (?), or exclamation mark (!)'
        }
        
        concept_lower = concept.lower()
        for key, explanation in concepts.items():
            if key in concept_lower or concept_lower in key:
                return explanation
        
        return f"No explanation found for '{concept}'. Try: subject-verb agreement, article, contraction, capitalization, punctuation"
    
    def correct(self, text):
        """
        Attempt to correct grammatical errors
        
        Args:
            text (str): Text to correct
            
        Returns:
            str: Corrected text
        """
        corrected = text.strip()
        
        # Capitalize first letter
        if corrected:
            corrected = corrected[0].upper() + corrected[1:]
        
        # Remove multiple spaces
        while '  ' in corrected:
            corrected = corrected.replace('  ', ' ')
        
        # Fix ending punctuation
        if corrected and corrected[-1] not in '.!?,;:':
            corrected += '.'
        
        return corrected
