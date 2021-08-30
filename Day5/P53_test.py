# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P53 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "abbac"
	out = "a:2, b:2, c:1"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))


def test_case2():
	inp = "8a*a**b%12"
	out = "8:1, a:2, *:3, b:1, %:1, 1:1, 2:1"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))


def test_case3():
	inp = "www.google.com"
	out = "w:3, .:2, g:2, o:3, l:1, e:1, c:1, m:1"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))

def test_case4():
	inp = "hello...."
	out = "h:1, e:1, l:2, o:1, .:4"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))

def test_case5():
	inp = "python is awesome!"
	out = "p:1, y:1, t:1, h:1, o:2, n:1,  :2, i:1, s:2, a:1, w:1, e:2, m:1, !:1"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))

def test_case6():
	inp = "1223334444"
	out = "1:1, 2:2, 3:3, 4:4"
	res = run(main, inp)
	assert (sorted(out) == sorted(res))

############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
