from lib.gen_pdf import compile_and_clean, generate_latex_from_csv

generate_latex_from_csv('405/005.csv', 'q1.tex')
compile_and_clean('q1.tex',clean=0)