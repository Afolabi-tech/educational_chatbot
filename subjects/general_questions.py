"""General questions module covering Nigeria and Telnet International Schools, Akure"""

class GeneralQuestions:
    """Handles general knowledge questions about Nigeria and Telnet International Schools, Akure"""
    
    def __init__(self):
        self.nigeria_facts = {
            'nigeria': 'Nigeria is a West African country with a population of over 200 million people. It is the most populous country in Africa.',
            'capital': 'The capital of Nigeria is Abuja, located in the center of the country.',
            'currency': 'The currency of Nigeria is the Nigerian Naira (₦).',
            'language': 'Nigeria has over 500 languages, with English as the official language. Major languages include Yoruba, Igbo, and Hausa.',
            'independence': 'Nigeria gained independence from British colonial rule on October 1, 1960.',
            'regions': 'Nigeria is divided into 36 states plus the Federal Capital Territory (FCT).',
            'ondo state': 'Ondo State is located in the southwestern part of Nigeria, known for agriculture, cocoa, and timber production.',
            'akure': 'Akure is the capital city of Ondo State, Nigeria. It is known for its educational institutions and cultural heritage.',
            'population': 'Nigeria has over 200 million inhabitants, making it the most populous nation in Africa.',
            'largest economy': 'Nigeria has the largest economy in Africa and is rich in natural resources, particularly oil and gas.',
            'government': 'Nigeria operates as a federal presidential republic with a bicameral legislature.',
            'president': 'As of 2024, Bola Ahmed Tinubu is the President of Nigeria. He was sworn in on May 29, 2023.',
            'national anthem': 'The Nigerian national anthem is "Arise, O Compatriots".',
            'flag': 'The Nigerian flag has three horizontal stripes: green, white, and green, symbolizing agriculture and hope.'
        }
        
        self.telnet_facts = {
            'telnet': 'Telnet International Schools is a leading educational institution in Akure, Ondo State, Nigeria, opened in September 2016.',
            'telnet international schools': 'Telnet International Schools, Akure offers quality education from Creche to High School levels with both day and boarding facilities.',
            'akure school': 'Telnet International Schools in Akure is known for its commitment to academic excellence and character development using hi-tech telecommunication systems.',
            'education': 'Telnet International Schools provides comprehensive education including academics, sports, debates, socials and travels.',
            'history': 'Telnet International School, Akure was opened in September 2016 with the aim of enhancing academically sound and godly young individuals. It started with Creche, Pre-Nursery, Nursery and Years One–Five in Primary and Years Seven and Eight in High School.',
            'mission': 'Provision of quality education by seasoned professionals in a conducive learning environment and in partnership with parents. Values of integrity, hard-work and honesty ensure development of children into responsible adults who become self-sufficient and confident leaders.',
            'vision': 'To be better than the best school in Nigeria by employing hi-tech Telecommunication and Networking System in teaching and learning. The school aims to be the school of choice, most admired for its location, people and performances.',
            'facilities': 'Telnet International Schools is equipped with modern facilities including classrooms, laboratories, library, sports grounds, boarding houses for students.',
            'location': 'Telnet International Schools is located in Akure, the capital of Ondo State, Nigeria.',
            'curriculum': 'Telnet International Schools exposes students to Nigerian and UK Curricula to create opportunities for admission to local and international higher education institutions.',
            'boarding': 'Telnet International Schools offers both day and boarding facilities. Half of the High School pupils are in the boarding house, while the other half are day students.',
            'objectives': 'Strategic objectives include: using hi-tech Telecommunication and Networking in teaching, providing conducive learning environment, encouraging mutual respect, creating collaboration between school and parents, employing seasoned professionals, exposing students to Nigerian and UK Curricula.',
            'extracurricular': 'Extra-curricular activities at Telnet International Schools include sports, debates, socials and travels to enhance student development.',
            'values': 'Integrity, hard-work and honesty are the core values of Telnet International Schools.',
            'teaching': 'Telnet International Schools employs the name TEL-NET to reflect its use of hi-tech Telecommunication and Networking devices in teaching and learning processes.'
        }
        
        # Management team information
        self.management_team = {
            'director': 'Dr. Joseph Kolawole Ariyo is the Director and co-founder of Telnet International Schools. He graduated from the University of Ilorin and retired as an Emergency Doctor at Chevron Nigeria Limited. Dr. Ariyo insists that God is the original founder of the School.',
            'joseph kolawole ariyo': 'Dr. Joseph Kolawole Ariyo is the Director and co-founder of Telnet International Schools. He graduated from the University of Ilorin and retired as an Emergency Doctor at Chevron Nigeria Limited.',
            'dr ariyo': 'Dr. Joseph Kolawole Ariyo is the Director and co-founder of Telnet International Schools.',
            'ariyo': 'Dr. Joseph Kolawole Ariyo is the Director and co-founder of Telnet International Schools.',
            'general manager': 'Miss Jane Edet is the General Manager of Telnet International Schools, effective August 1, 2026. She holds a B.Sc. in Biochemistry from Madonna University and an M.Tech in Biochemistry from Federal University of Technology, Akure. She joined Telnet in 2016 and has served as primary school teacher, laboratory attendant, Assistant Head Mistress, and Head of Primary School.',
            'jane edet': 'Miss Jane Edet is the General Manager of Telnet International Schools, effective August 1, 2026. She holds a B.Sc. in Biochemistry from Madonna University and an M.Tech in Biochemistry from Federal University of Technology, Akure. She joined Telnet in 2016 and has served as primary school teacher, laboratory attendant, Assistant Head Mistress, and Head of Primary School.',
            'head of primary school': 'Mr. Odunayo Shittu is the Head of Primary School at Telnet International Schools, effective August 1, 2026. He obtained his B.Tech in Microbiology from Federal University of Technology, Akure in 2016. He joined Telnet International Schools in 2018 and was promoted to Head of Primary School from Assistant Head Teacher.',
            'odunayo shittu': 'Mr. Odunayo Shittu is the Head of Primary School at Telnet International Schools, effective August 1, 2026. He obtained his B.Tech in Microbiology from Federal University of Technology, Akure in 2016. He joined Telnet International Schools in 2018 and was promoted to Head of Primary School from Assistant Head Teacher.',
            'assistant head of primary school': 'Mrs. Opeyemi Oladehinde is the Assistant Head of Primary School at Telnet International Schools, effective August 1, 2026. She obtained her B.Sc. Agriculture (Plant Science) from Obafemi Awolowo University, Ile-Ife in 2008. She joined Telnet International Schools in January 2021 as a primary school class teacher.',
            'opeyemi oladehinde': 'Mrs. Opeyemi Oladehinde is the Assistant Head of Primary School at Telnet International Schools, effective August 1, 2026. She obtained her B.Sc. Agriculture (Plant Science) from Obafemi Awolowo University, Ile-Ife in 2008. She joined Telnet International Schools in January 2021 as a primary school class teacher.',
            'principal': 'Mrs. Tolulope Adewumi is the Principal of Telnet International Schools. She obtained her B.Sc. Geophysics from Adekunle Ajasin University, Akungba and M.Tech in Geophysics from Federal University of Technology, Akure. She joined Telnet in 2018 and was promoted to Vice Principal in 2023 and then to Principal.',
            'tolulope adewumi': 'Mrs. Tolulope Adewumi is the Principal of Telnet International Schools. She obtained her B.Sc. Geophysics from Adekunle Ajasin University, Akungba and M.Tech in Geophysics from Federal University of Technology, Akure. She joined Telnet in 2018 and was promoted to Vice Principal in 2023 and then to Principal.',
            'vice principal': 'Mr. Joseph Oluwasogo Bello is the Vice Principal of Telnet International Schools. He obtained his B.Tech in Geophysics from Federal University of Technology, Akure in 2017. He joined Telnet International Schools in September 2020 and was promoted to Vice Principal in 2023.',
            'joseph oluwasogo bello': 'Mr. Joseph Oluwasogo Bello is the Vice Principal of Telnet International Schools. He obtained his B.Tech in Geophysics from Federal University of Technology, Akure in 2017. He joined Telnet International Schools in September 2020 and was promoted to Vice Principal in 2023.',
            'sogo': 'Mr. Joseph Oluwasogo Bello (Sogo) is the Vice Principal of Telnet International Schools. He obtained his B.Tech in Geophysics from Federal University of Technology, Akure in 2017. He joined Telnet International Schools in September 2020 and was promoted to Vice Principal in 2023.',
            'management': 'Telnet International Schools leadership includes: Director - Dr. Joseph Kolawole Ariyo, General Manager - Miss Jane Edet, Head of Primary School - Mr. Odunayo Shittu, Assistant Head of Primary School - Mrs. Opeyemi Oladehinde, Principal - Mrs. Tolulope Adewumi, Vice Principal - Mr. Joseph Oluwasogo Bello.',
            'staff': 'Telnet International Schools leadership includes: Director - Dr. Joseph Kolawole Ariyo, General Manager - Miss Jane Edet, Head of Primary School - Mr. Odunayo Shittu, Assistant Head of Primary School - Mrs. Opeyemi Oladehinde, Principal - Mrs. Tolulope Adewumi, Vice Principal - Mr. Joseph Oluwasogo Bello.'
        }
    
    def answer(self, question):
        """
        Answer general knowledge questions
        
        Args:
            question (str): General knowledge question
            
        Returns:
            str: Answer to the question
        """
        question_lower = question.lower()
        
        # Check for most specific keywords first to avoid partial matches
        specific_keywords = ['vice principal', 'general manager', 'assistant head', 'head of primary', 'president', 'director', 'ariyo']
        for keyword in specific_keywords:
            if keyword in question_lower:
                # For "assistant head", check the management_team
                if keyword == 'assistant head' and 'assistant head of primary school' in self.management_team:
                    return self.management_team['assistant head of primary school']
                # For "head of primary", check the management_team  
                if keyword == 'head of primary' and 'head of primary school' in self.management_team:
                    return self.management_team['head of primary school']
                # For other keywords, check both dictionaries
                if keyword in self.management_team:
                    return self.management_team[keyword]
                if keyword in self.nigeria_facts:
                    return self.nigeria_facts[keyword]
        
        # Check against management team
        for concept, explanation in self.management_team.items():
            if concept in question_lower:
                return explanation
        
        # Check for specific Telnet facts first (before general 'telnet')
        specific_telnet_keywords = ['vision', 'mission', 'history', 'boarding', 'objectives', 'extracurricular', 'teaching', 'values', 'curriculum']
        for keyword in specific_telnet_keywords:
            if keyword in question_lower:
                if keyword in self.telnet_facts:
                    return self.telnet_facts[keyword]
        
        # Check against all Telnet facts
        for concept, explanation in self.telnet_facts.items():
            if concept in question_lower:
                return explanation
        
        # Check against Nigeria facts
        for concept, explanation in self.nigeria_facts.items():
            if concept in question_lower:
                return explanation
        
        return "I can help with questions about Nigeria, Akure, Ondo State, Telnet International Schools, and our management team. Ask me about any staff member or school information!"
    
    def explain_region(self, region_name):
        """
        Explain Nigerian regions or states
        
        Args:
            region_name (str): Name of the region or state
            
        Returns:
            str: Explanation of the region
        """
        regions = {
            'ondo state': 'Ondo State is located in southwestern Nigeria. It is known for cocoa production, timber, and agricultural products. The state is home to several educational institutions including Telnet International Schools in Akure.',
            'akure': 'Akure is the capital city of Ondo State. It is a major commercial and educational hub in the region, home to Telnet International Schools and other tertiary institutions.',
            'southwest': 'The Southwest region includes states like Lagos, Oyo, Osun, Ekiti, and Ondo. It is known for its rich cultural heritage and economic activity.'
        }
        
        return regions.get(region_name.lower(), f"Region {region_name} not found in database.")
    
    def get_school_info(self, info_type):
        """
        Get specific information about Telnet International Schools
        
        Args:
            info_type (str): Type of information requested
            
        Returns:
            str: Information about the school
        """
        school_info = {
            'vision': 'To develop globally competitive students with strong academic foundation and moral values.',
            'values': 'Integrity, Excellence, Discipline, and Commitment are the core values of Telnet International Schools.',
            'programs': 'Telnet International Schools offers diverse programs including academic excellence, sports development, arts, and character formation.',
            'achievement': 'Telnet International Schools has a track record of producing well-rounded graduates who excel in tertiary institutions.'
        }
        
        return school_info.get(info_type.lower(), f"Information about {info_type} not found in database.")
