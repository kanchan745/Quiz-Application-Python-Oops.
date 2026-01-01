class Quiz:
    def __init__(self):
        self.score = 0
    
    def question (self,ques,options, correct_ans):
        print("\n"+ques) 
        for opt in options:
            print(opt)
            
        answer = input("Enter your answer: ")
        
        if answer == correct_ans:
            print("Correct Answer!")
            self.score += 1
        else:
            print("Wrong Answer!")
    
    def show_score(self):
        print("\n Your final score is:",self.score)
        
quiz = Quiz()
quiz.question("What is the capital of India? ",["a) Mumbai","b)New Delhi","c)Kolkata","d)Chennai"],"b")

quiz.question("What is the symbol is used for comments in Python?",["a)//","b)/* */","c)#","d)/"],"c")

quiz.question("Which of the following is a Python data type?",["a)integer","b)string","c)list","d)All of the above"],"d")            

quiz.question("Which keyword is used to create a function in Python?",["a)func","b)def","c)function","d)define"],"b") 

quiz.question("Which of the following is used to define a block of code in Python?",["a)Brackets","b)Indentation","c)Parentheses","d)Quotes"],"b")  

quiz.show_score()   