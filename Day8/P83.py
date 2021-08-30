############################[ IMMUTABLE CODE SECTION BEGIN ]#############################
# ------------------------------------------------------------------------------------- #
# helper library functions                                                              #
import pandas as pd                                                                     #                             
import sys, os, getpass                                                                 #
#                                                                                       #
sys.path.insert(0, "..")  # add to search path to enable discovery of our module        #
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))   #
from Util.misc import NaN, FIRST, SECOND, THIRD, FOURTH, SIXTH,\
    Event, InvalidInputException, create_empty_dataframe, clear, wait                   #
from P83_helper import login_header, home_header, add_students_header, \
    update_records_header, display_records_header, multiple_records_header              #
# ------------------------------------------------------------------------------------- #
############################[ IMMUTABLE CODE SECTION BEGIN ]#############################


class StudentGradingSystem(object):

    max_marks = [20, 100, 100, 50]          # for Quiz, Exam, Assignment, Project in order
    weightage = [0.15, 0.40, 0.20, 0.25]

    # database schema for storing student records
    column_names = ['Roll_No', 'Quiz', 'Exam', 'Assignment', 'Project', 'GPA', 'Grade']
    data_types = [str, float, float, float, float, float, str]   
    records_file_name = "results.csv"
    database = create_empty_dataframe(columns=column_names, dtypes=data_types)

    @classmethod
    def login(cls):
        """Accept user id/ type of user.
        Create appropriate object."""
        
        pass

    @classmethod
    def validate_student_roll_no(cls, roll_no):
        """Raise an exception if roll_no not found in database."""

        pass

    @classmethod
    def validate_and_parse_marks(cls, raw_input):
        """Validate and parse input marks."""
        
        pass

    @classmethod
    def create_student_row(cls, roll_no=NaN, quiz=NaN, exam=NaN, \
        assignment=NaN, project=NaN, gpa=NaN, grade=NaN):
        """Return a new Series (student row) based on input values."""
        
        pass

    @classmethod
    def read_database_file(cls, records_file):
        """Read student records from a database file."""

        pass

    @classmethod
    def add_students_from_file(cls, user_id):
        """Add students records read from a database file."""

        pass

    @classmethod
    def read_marks_from_file(cls, user_id):
        """Update student records read from a database file."""
        
        pass

    @classmethod
    def add_students_manually(cls):
        """Add student records from user input."""

        pass

    @classmethod
    def read_marks_manually(cls):
        """Update student records from user input."""

        pass

    @classmethod
    def display_single_record(cls, roll_no):
        """Display a student record read from records file."""
        
        pass


    def compute_gpa(self, assign=False):
        """Compute and update GPA/ assign Grade of student record."""

        pass

    @staticmethod
    def assign_grade(gpa):
        pass

    @staticmethod
    def logout():
        """Exit the system."""

        pass


class User(object):

    # define constructor

    def display_record(self, roll_no=None):
        """Fetch and display student record(s)."""

        pass

class Instructor(User):

    def add_students(self):
        """Add student records from file or user input."""

        pass

    def read_marks(self):
        """Update student records from file or user input."""

        pass

    def compute_gpa(self, assign=False):
        """Compute and update GPA/ assign Grade of student record."""

        pass

    def generate_records(self):
        """Dump in-memory student records to records file."""
        
        pass

class Ta(Instructor):

    # hide read_marks capability

    pass

class Student(User):
    
    # override display_record

    pass


#######[ IMMUTABLE CODE SECTION BEGIN ]#######
# ------------------------------------------ #
def main():                                  #
# ------------------------------------------ #
########[ IMMUTABLE CODE SECTION END ]########

    # grader = StudentGradingSystem

    # user = grader.login()

    while True:

        # display menu

        # read input choice
        
        # take appropriate action

        # handle errors

        pass


#######[ IMMUTABLE CODE SECTION BEGIN ]#######
# ------------------------------------------ #
# Using the special variable __name__        #
if __name__ == "__main__":                   #
    main()                                   #
# ------------------------------------------ #
########[ IMMUTABLE CODE SECTION END ]########
