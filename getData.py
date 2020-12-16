import pandas as pd
from datetime import datetime
import os.path

# 3 attributes for the class Question
class Question:
    def __init__(self, question_type, question_text, question_summary):
        self.question_type = question_type
        self.question_text = question_text
        self.question_summary = question_summary

# this function returns the question type
    @property
    def question_type(self):
        return self._question_type

# this function checks the validity of question type
    @question_type.setter
    def question_type(self, qt):
        if not (qt == "yes_no" or qt == "scale" or qt == "hours"):
            raise Exception("invalid question type")
        self._question_type = qt

# this functions the questions that the user has to answer
def input_data():
    # add new Questions here
    questions = [Question("scale", "How do you feel? [from 1-10]", "Happiness"),
                 Question("hours", "How many hours of sleep did you get? [in hours]", "Sleep"),
                 Question("hours", "How long did you work today? [in hours]", "Work"),
                 Question("yes_no", "Did you eat something warm today? [yes/no]", "Warm Meal"),
                 Question("yes_no", "Did pleasure yourself? [yes/no]", "Pleasure"),
                 Question("yes_no", "Did you do some sport today? [yes/no]", "Sport"),
                 Question("hours", "How long have you been outside today? [in hours]", "Outdoor"),
                 Question("yes_no", "Did you drink alcohol today? [yes/no]", "Alcohol"),
                 Question("yes_no", "Did you see some friends today? [yes/no]", "Friends"),
                 Question("yes_no", "Did you have an experience of success today? [yes/no]", "Success Experience")]

# this code checks if the answer is in a valid form
    answers = []
    # loop through all questions
    for question in questions:
        invalid_input = True

        # repeat questioning until valid input
        while invalid_input:

            print(question.question_text)
            text = input('Answer: ')

            # checks if answer is yes or no
            if question.question_type == "yes_no":
                if text.upper() == "YES" or text.upper() == "NO":
                    print("valid input!")
                    invalid_input = False
                else:
                    print("invalid input! enter yes/no ")

            # checks if answer is between 1-10
            if question.question_type == "scale":
                try:
                    text = int(text)
                    if 1 <= text <= 10:
                        invalid_input = False
                except ValueError:
                    print("please enter number 1 - 10")

            # checks if answer is between 0-24 hours
            if question.question_type == "hours":
                try:
                    text = float(text)
                    if 0 <= text <= 24:
                        invalid_input = False
                except ValueError:
                    print("please enter number 0 - 24")
        # add the valid answer to the list of answers
        answers.append(text)

    # add current date
    now = datetime.now()
    date_now = now.strftime("%d/%m/%Y %H:%M:%S")
    answers.append(date_now)

    # create column names of row/file
    columns = []
    for question in questions:
        columns.append(str(question.question_summary))
    columns.append('Date')

    # create new row
    row = pd.DataFrame(data=[answers], columns=columns)

    # check if file exists
    if not os.path.isfile('data_file.pkl'):
        # store new file
        row.to_pickle('data_file.pkl')
    else:
        # append new row to file and store
        table = pd.read_pickle('data_file.pkl')
        table = table.append(row, ignore_index=True)
        table.to_pickle('data_file.pkl')

    # check file
    solution = pd.read_pickle('data_file.pkl')
    print(solution)
