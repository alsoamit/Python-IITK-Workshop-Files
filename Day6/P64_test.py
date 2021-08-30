# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P64 import main

############ TEST CASES BEGIN ############


def test_case1():
	f = open("results.txt",'r')
	A = f.read()
	B='''Roll_No Quiz Exam Assignment Project GPA Grade\nMaxMarks 20 100 100 50 None None\nWeight 15 40 20 25 None None\n101 0 55 60 43.5 5.58 D\n102 19 96 94.5 45.5 9.43 A\n103 7 92 86 30 7.43 C\n104 0 78 0 39 5.07 D\n105 15 83.5 80 45 8.31 B\n106 16 88 90 48 8.92 B\n108 4 59 60 45 6.11 D\n109 20 95 95 41.5 9.28 A\n110 13 61 74 30 6.4 D\n'''
	assert(B==A)


############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
