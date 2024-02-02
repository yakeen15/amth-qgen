import subprocess
import os
import pandas as pd
import random

def create_temp_csv(csv_files, num_questions):
    temp_data = {'QuestionID': [], 'QuestionText': []}
    
    for csv_file, num_questions_per_file in zip(csv_files, num_questions):
        df = pd.read_csv(csv_file)
        
        selected_questions = []
        df = df.dropna()
        print(df)
        if num_questions_per_file > len(df):
            selected_questions = df['QuestionText'].tolist()
        else:
            selected_questions = random.sample(df['QuestionText'].tolist(), num_questions_per_file)
        
        prefix = csv_file.split('.')[0]
        new_question_ids = [f"{prefix}_{i+1}" for i in range(num_questions_per_file)]
        
        temp_data['QuestionID'].extend(new_question_ids)
        temp_data['QuestionText'].extend(selected_questions)
    
    temp_df = pd.DataFrame(temp_data)
    
    temp_df.to_csv('temp.csv', index=False)

def generate_latex_from_csv(csv_path, output_latex_path):
    df = pd.read_csv(csv_path)
    with open(output_latex_path, 'w') as latex_file:
        latex_file.write(r'\documentclass{article}' + '\n')
        latex_file.write(r'\usepackage{tabularx}' + '\n')
        latex_file.write(r'\usepackage{amssymb}' + '\n')
        latex_file.write(r'\begin{document}' + '\n')
        question_id = 0
        for index, row in df.iterrows():
            question_id = question_id+1
            question_text = row['QuestionText']
            latex_file.write(r'\section*{Question ' + str(question_id) + '}' + '\n')
            latex_file.write(rf'{question_text}' + '\n')
        latex_file.write(r'\end{document}' + '\n')

    print(f"LaTeX file '{output_latex_path}' generated successfully.")
def compile_and_clean(file_path,clean=0):
    try:
        subprocess.run(['pdflatex', file_path])
        base_name = os.path.splitext(file_path)[0]
        aux_extensions = ['.aux', '.txt', '.log', '.tex']
        if clean==0:
            for ext in aux_extensions:
                aux_file = base_name + ext
                if os.path.exists(aux_file):
                    os.remove(aux_file)

        print("Compilation and cleanup successful.")
    except Exception as e:
        print(f"Error during compilation: {e}")

