# P42

quiz_max, exam_max, assignment_max, project_max = 20, 100, 100, 50

def inputCheck(type, type_max):
    # Checking input
    if type > type_max:
        return ("ERROR: Invalid Marks {} > {}".format(type, type_max))
    elif type < 0:
        return ("ERROR: Invalid Marks {} < {}".format(type, 0))

def read_marks():
    # Take and check inputs for the four assessments
    quiz = int(input())
    test = inputCheck(quiz, quiz_max)
    if test:
        print(test)
        return
        
    exam = int(input())
    test = inputCheck(exam, exam_max)
    if test:
        print(test)
        return

    assignment = int(input())
    test = inputCheck(assignment, assignment_max)
    if test:
        print(test)
        return

    project = int(input())
    test = inputCheck(project, project_max)
    if test:
        print(test)
        return
    
    return [quiz, exam, assignment, project]

# computing GPA of the valid marks
def compute_gpa(quiz,exam,assignment,project):
    quiz_wei, exam_wei, assignment_wei, project_wei = 15, 40, 20, 25
    return ((quiz / quiz_max)*quiz_wei + (exam / exam_max)*exam_wei + (assignment / assignment_max)*assignment_wei + (project / project_max)*project_wei)/10

# assigning grade according to the GPA
def assign_grade(gpa):
    if gpa == 10:
        return "O"
    elif gpa >= 9 and gpa < 10:
        return "A"
    elif gpa >= 8 and gpa < 9:
        return "B"
    elif gpa >= 6.5 and gpa < 8:
        return "C"
    elif gpa >= 5 and gpa < 6.5:
        return "D"
    elif gpa < 5:
        return "F"

def main():
    # take input and call functions
    inputs = read_marks()
    if inputs:
        quiz, exam, assignment, project = read_marks()
    else:
        return
    gpa = round(compute_gpa(quiz, exam, assignment, project), 2)
    grade = assign_grade(gpa)
    print("The GPA IS {}, and the Grade is {}".format(gpa, grade))

if __name__ == "__main__":
    main()
