from lib.gen_pdf import compile_and_clean, generate_latex_from_csv, create_temp_csv
import pandas as pd
import os

def parse_input(input_data):
    pairs = input_data.split("),(")

    pairs = [tuple(map(int, pair.replace("(", "").replace(")", "").split(','))) for pair in pairs]

    first_elements = [pair[0] for pair in pairs]
    second_elements = [pair[1] for pair in pairs]

    return [first_elements, second_elements]

def list_topic(csv_file):    
    if not os.path.exists(csv_file):
        print("File 'index.csv' not found in the specified directory.")
        return
    
    df = pd.read_csv(csv_file)
    return df

def list_course():
    current_directory = os.getcwd()
    courses = []
    folders_starting_with_4 = []
    for folder in os.listdir(current_directory):
        if os.path.isdir(os.path.join(current_directory, folder)) and folder.startswith('4'):
            folders_starting_with_4.append(folder)
    
    if folders_starting_with_4:
        i=1
        for folder in folders_starting_with_4:
            courses.append(folder)
            i=i+1
    else:
        print("No folders starting with '4' found in the directory.")
    return courses

def gen_interface():
    while True:
        courses = list_course()
        i=1
        for course in courses:
            print(str(i)+'. '+course)
            i=i+1
        print("Enter which course you would like to generate questions for (x to exit)")
        choice = input()
        if choice=='x':
            break
        else:
            choice = int(choice)
            directory = courses[choice-1]
            csv_file = os.path.join(directory, "index.csv")
            df = list_topic(csv_file)
            print("Available topics on the course")
            print(df.to_string(index=False))
            print("Enter an ordered pair (n,m) where n is the topic id and m is the number of questions to be generated from the said topic")
            topics = input()
            p_topics = parse_input(topics)
            topics = p_topics[0]
            num_q = p_topics[1]
            qname = input('Enter the name of the file: ')
            if '.tex' not in qname:
                qname=qname+'.tex'
            files = os.listdir(directory)
            topic_list = []
            for i in topics:
                topic_list.append(directory+r'/'+files[i])
            create_temp_csv(topic_list,num_q)
            generate_latex_from_csv('temp.csv',qname)
            compile_and_clean(qname)

gen_interface()