import csv
import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

def read_question_set(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        question_set = [row for row in reader]
    return question_set

def generate_random_question_set(question_set, num_questions):
    return random.sample(question_set, num_questions)

def render_latex(expression):
    fig, ax = plt.subplots(figsize=(4, 1))
    ax.text(0.5, 0.5, f"${expression}$", size=16, color='black',
            ha='center', va='center')
    ax.axis('off')
    plt.tight_layout()
    plt.show()

# Example usage
file_path = 'q1.csv'
all_questions = read_question_set(file_path)
num_questions_to_generate = 1
random_questions = generate_random_question_set(all_questions, num_questions_to_generate)

for question in random_questions:
    print(f"Question: {question['QuestionText']}")
    print(f"Options: {question['Options']}")
    print(f"Correct Answer: {question['CorrectAnswer']}")
    render_latex(question['QuestionText'])
