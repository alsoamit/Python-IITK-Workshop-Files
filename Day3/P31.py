# P31

def main():
    # Write your code below
    quiz_max, exam_max, assignment_max, project_max = 20, 100, 100, 50
    quiz_wei, exam_wei, assignment_wei, project_wei = 15, 40, 20, 25
    # Take inputs for the four assessments
    quiz = int(input())

    # Checking first input
    if quiz > quiz_max:
        print("ERROR: Invalid Marks {} > {}".format(quiz, quiz_max))
        return
    elif quiz < 0:
        print("ERROR: Invalid Marks {} < {}".format(quiz, 0))
        return

    exam = int(input())
    if exam > exam_max:
        print("ERROR: Invalid Marks {} > {}".format(exam, exam_max))
        return
    elif exam < 0:
        print("ERROR: Invalid Marks {} < {}".format(exam, 0))
        return

    assignment = int(input())
    if assignment > assignment_max:
        print("ERROR: Invalid Marks {} > {}".format(assignment, assignment_max))
        return
    elif assignment < 0:
        print("ERROR: Invalid Marks {} < {}".format(assignment, 0))
        return

    project = int(input())
    if project > project_max:
        print("ERROR: Invalid Marks {} > {}".format(project, project_max))
        return
    elif project < 0:
        print("ERROR: Invalid Marks {} < {}".format(project, 0))
        return

    # Calculate the GPA.
    GPA = ((quiz / quiz_max)*quiz_wei + (exam / exam_max)*exam_wei + (assignment / assignment_max)*assignment_wei + (project / project_max)*project_wei)/10

    # Round the GPA to two decimal places and print it
    GPA = round(GPA, 2)
    print(GPA)

if __name__ == "__main__":
    main()