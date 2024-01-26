import subprocess
import os
import pandas as pd

def generate_latex_from_csv(csv_path, output_latex_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Open the LaTeX file for writing
    with open(output_latex_path, 'w') as latex_file:
        # Write the preamble of the LaTeX document
        latex_file.write(r'\documentclass{article}' + '\n')
        latex_file.write(r'\usepackage{tabularx}' + '\n')
        latex_file.write(r'\begin{document}' + '\n')

        # Iterate through each row in the DataFrame
        question_id = 0
        for index, row in df.iterrows():
            question_id = question_id+1
            question_text = row['QuestionText']

            # Write a new section for each question
            latex_file.write(r'\section*{Question ' + str(question_id) + '}' + '\n')
            latex_file.write(rf'{question_text}' + '\n')

        # Write the end of the LaTeX document
        latex_file.write(r'\end{document}' + '\n')

    print(f"LaTeX file '{output_latex_path}' generated successfully.")
def compile_and_clean(file_path,clean=0):
    try:
        # Run pdflatex command to compile the LaTeX file
        subprocess.run(['pdflatex', file_path])

        # Clean up auxiliary files
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

