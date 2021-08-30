######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
# import numpy as np
# from scipy import linalg
import sys, os
from typing import Tuple

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


temp_records=dict()
final_records=dict()
total=[20,100,100,50]
quiz, exam, assignment, project = [0, 0, 0, 0]
quiz_max, exam_max, assignment_max, project_max = [20, 100, 100, 50]

def inputCheck(type, type_max):
    # Checking input
    if type > type_max:
        return ("ERROR: Invalid Marks {}.0 > {}".format(type, type_max))
    elif type < 0:
        return ("ERROR: Invalid Marks {}.0 < {}".format(type, 0))

def add_student():
    while True:
        inp = int(input())
        if inp == -1:
            break
        temp_records[inp] = 0
    

def read_marks(err_in_reading):
    roll = int(input())
    global quiz, exam, assignment, project

    if roll in temp_records.keys():
        # Take and check inputs for the four assessments
        quiz = int(input())
        test = inputCheck(quiz, quiz_max)
        if test:
            print(test)
            err_in_reading[0] = True
            return

        exam = int(input())
        test = inputCheck(exam, exam_max)
        if test:
            print(test)
            err_in_reading[0] = True
            return

        assignment = int(input())
        test = inputCheck(assignment, assignment_max)
        if test:
            print(test)
            err_in_reading[0] = True
            return

        project = int(input())
        test = inputCheck(project, project_max)
        if test:
            print(test)
            err_in_reading[0] = True
            return

        temp_records[roll] = {"list_of_marks" : [quiz, exam, assignment, project], "GPA" : 0, "grade" : ""}
    else:
        print("ERROR: Student roll number does not exist")

def compute_gpa():
    roll = int(input())
    if roll in temp_records.keys():
        if "list_of_marks" in temp_records[roll].keys():
            quiz_wei, exam_wei, assignment_wei, project_wei = 15, 40, 20, 25
            temp_records[roll]["GPA"] = ((quiz / quiz_max)*quiz_wei + (exam / exam_max)*exam_wei + (assignment / assignment_max)*assignment_wei + (project / project_max)*project_wei)/10
            assign_grade(temp_records[roll]["GPA"], roll)
        else:
            print("ERROR: Student roll number marks information unavailable")
    else:
        print("ERROR: Student roll number does not exist")


def assign_grade(gpa, roll):
    if gpa == 10:
        temp_records[roll]["grade"] =  "O"
    elif gpa >= 9 and gpa < 10:
        temp_records[roll]["grade"] =  "A"
    elif gpa >= 8 and gpa < 9:
        temp_records[roll]["grade"] =  "B"
    elif gpa >= 6.5 and gpa < 8:
        temp_records[roll]["grade"] =  "C"
    elif gpa >= 5 and gpa < 6.5:
        temp_records[roll]["grade"] =  "D"
    elif gpa < 5:
        temp_records[roll]["grade"] =  "F"

def generate_records():
    final_records.update(temp_records)


def display_records():
    roll = int(input())
    if roll in temp_records.keys():        
        print([round(float(x), 1) for x in temp_records[roll]["list_of_marks"]])
        print(round(float(temp_records[roll]["GPA"]), 2))
        print(temp_records[roll]["grade"])
    else:
        print("ERROR: Student roll number does not exist")

def main():
    def ask_for_input():
        err_in_reading = [False]
        inp = int(input())
        if inp == 1:
            add_student()
            ask_for_input()
        elif inp == 2:
            read_marks(err_in_reading)
            if err_in_reading[0]:
                return
            else:
                ask_for_input()
        elif inp == 3:
            compute_gpa()
            ask_for_input()
        elif inp == 4:
            generate_records()
            ask_for_input()
        elif inp == 5:
            display_records()
            ask_for_input()
        elif inp == 6:
            return
        else:
            print("ERROR: Invalid Command!")
    ask_for_input()

if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########