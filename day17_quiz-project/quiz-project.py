class Quiz:
    def __init__(self,questions = 0):
        self.questions = questions 
    
    def __repr__(self):
        return f"{self.questions}"
    
    def __str__(self):
        return f"{self.questions}"

    def __eq__(self,other):
        return self.questions==other.questions
    
    def __lt__(self,other):
        return self.questions<other.questions
    
    def __add__(self,other):
        return self.questions+other.questions
