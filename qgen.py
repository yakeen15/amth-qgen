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

def render_latex(ax, expression):
    ax.text(0.5, 0.5, f"{expression}", size=16, color='black',
            ha='center', va='center', fontfamily='serif')
    ax.axis('off')

# Example usage
file_path = 'q1.csv'
all_questions = read_question_set(file_path)
num_questions_to_generate = 5
random_questions = generate_random_question_set(all_questions, num_questions_to_generate)

# Adjust the bottom and top parameters using gridspec_kw
fig, axes = plt.subplots(nrows=num_questions_to_generate, ncols=1, figsize=(8, 15),
                         gridspec_kw={'bottom': 0.15, 'top': 0.9, 'hspace': 0.4})  # Added hspace for better spacing

for idx, question in enumerate(random_questions):
    question_text = question['QuestionText']
    
    axes[idx].text(-0.1, 0.5, f"Question {idx+1}", rotation=90, ha='right', va='center', fontsize=12)
    render_latex(axes[idx], question_text)

plt.tight_layout()
plt.show()
