# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P62 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "__x123\n1"
	out = "Item 1 found in __x123A.txt"
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = "__000\nmyItem"
	out = "Item myItem found nowhere"
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = "__000\n__lt__"
	out = "Item __lt__ found in both __000A.txt and __000B.txt"
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = "__axbyczd\n0"
	out = "Item 0 found in __axbyczdB.txt"
	res = run(main, inp)
	assert (out == res)


############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)




