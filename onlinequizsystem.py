# Define the Question class
class Question:
    def __init__(self, prompt, options, correct_answer_index):
        self.prompt = prompt  # The text of the question
        self.options = options  # A list of possible answer options
        self.correct_answer_index = correct_answer_index  # The 0-based index of the correct option

    def display(self):
        print(f"\n{self.prompt}")
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def is_correct(self, user_answer_index):
        return user_answer_index == self.correct_answer_index
# Define the Quiz class
class Quiz:
    def __init__(self, name, questions):
        self.name = name  # Name of the quiz
        self.questions = questions  # List of Question objects for this quiz
        self.score = 0

    def run_quiz(self):
        print(f"\n--- Starting {self.name} ---")
        self.score = 0
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}:")
            question.display()
            while True:
                try:
                    user_input = int(input("Select your answer (enter the number): ")) - 1 # Convert to 0-based index
                    if 0 <= user_input < len(question.options):
                        break
                    else:
                        print("Invalid option. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if question.is_correct(user_input):
                print("Correct answer!")
                self.score += 1
            else:
                print(f"Wrong answer. The correct answer was: {question.options[question.correct_answer_index]}")
        
        print(f"\n--- {self.name} Ended --- ")
        print(f"Your total score: {self.score} out of {len(self.questions)}")
# --- Demonstration of a Simple Quiz --- 

# 1. Create Question objects
q1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2) # Paris is at index 2
q2 = Question("Which planet is known as the 'Blue Planet'?", ["Mars", "Earth", "Jupiter", "Venus"], 1) # Earth is at index 1
q3 = Question("What is 7 multiplied by 8?", ["49", "54", "56", "63"], 2) # 56 is at index 2
q4 = Question("Which of these is a programming language?", ["Excel", "Word", "Python", "PowerPoint"], 2) # Python is at index 2

# 2. Create a Quiz object with the questions
my_basic_quiz = Quiz("General Knowledge Quiz", [q1, q2, q3, q4])

# 3. Run the quiz
my_basic_quiz.run_quiz()