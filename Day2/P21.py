# P21

def main():
    # Write your code below
    quiz_max, exam_max, assignment_max, project_max = 20, 100, 100, 50
    quiz_wei, exam_wei, assignment_wei, project_wei = 15, 40, 20, 25
    # Take inputs for the four assessments
    quiz = int(input())
    exam = int(input())
    assignment = int(input())
    project = int(input())

    # Calculate the GPA.
    GPA = ((quiz / quiz_max)*quiz_wei + (exam / exam_max)*exam_wei + (assignment / assignment_max)*assignment_wei + (project / project_max)*project_wei)/10

    # Round the GPA to two decimal places and print it
    GPA = round(GPA, 2)
    print(GPA)

if __name__ == "__main__":
    main()