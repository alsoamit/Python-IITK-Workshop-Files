# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P52 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "The quick brown fox jumps over the lazy dog"
	out = "Yes, the string is a pangram."
	res = run(main, inp)
	assert (out == res)


def test_case2():
	inp = "The brown fox jump over the lazy dog"
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) c, i, k, q, s."
	res = run(main, inp)
	assert (out == res)


def test_case3():
	inp = "Hi, I am Amey"
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) b, c, d, f, g, j, k, l, n, o, p, q, r, s, t, u, v, w, x, z."
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = "Did The quick brown fox jump over the lazy dog, hmm ..., I don't know."
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) s."
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = "This problem has no automated test cases. Add automated/pre-generated test cases to this problem."
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) f, j, k, q, v, w, x, y, z."
	res = run(main, inp)
	assert (out == res)

def test_case6():
	inp = "..."
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z."
	res = run(main, inp)
	assert (out == res)

def test_case7():
	inp = "No, the string is NOT a pangram. Missing letter(s) is(are) a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z."
	out = "Yes, the string is a pangram."
	res = run(main, inp)
	assert (out == res)

def test_case8():
	inp = "Yes, the string is a pangram."
	out = "No, the string is NOT a pangram. Missing letter(s) is(are) b, c, d, f, j, k, l, o, q, u, v, w, x, z."
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
