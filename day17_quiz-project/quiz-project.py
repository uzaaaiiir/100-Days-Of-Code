class Quiz:
    def __init__(self,questions = 0):
        self.questions = questions 
    
    def __repr__(self):
        return f"{self.questions}"