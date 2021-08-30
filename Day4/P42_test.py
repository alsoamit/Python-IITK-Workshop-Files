import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P42_solution import main
from P42 import main 

def testcase1() -> None:
    inp='''18
           80
           90
           54'''
    out='''ERROR: Invalid Marks 54 > 50'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''18
           80
           90
           45'''
    out='''The GPA is 8.6, and the Grade is B'''
    res=run(main,inp)
    assert(res==out)

def testcase3():
	inp = '''20\n100\n100\n50'''
	out = '''The GPA is 10.0, and the Grade is O'''
	res = run(main, inp)
	assert (out == res)

def testcase4():
	inp = '''0\n27\n41\n13'''
	out = '''The GPA is 2.55, and the Grade is F'''
	res = run(main, inp)
	assert (out == res)

def testcase5():
	inp = '''19\n99\n99\n49'''
	out = '''The GPA is 9.81, and the Grade is A'''
	res = run(main, inp)
	assert (out == res)

def testcase6():
	inp = '''1\n80\n61\n11'''
	out = '''The GPA is 5.05, and the Grade is D'''
	res = run(main, inp)
	assert (out == res)

def testcase7() -> None:
    inp='''15
           102
           -90
           56'''
    out='''ERROR: Invalid Marks 102 > 100'''
    res=run(main,inp)
    assert(res==out)

def testcase8() -> None:
    inp='''15
          -102
          -90
          56'''
    out='''ERROR: Invalid Marks -102 < 0'''
    res=run(main,inp)
    assert(res==out)
    
def testcase9() -> None:
    inp='''17
           100
           100
           -50'''
    out='''ERROR: Invalid Marks -50 < 0'''
    res=run(main,inp)
    assert(res==out)

def testcase10() -> None:
    inp='''20
           100
           150
           0'''
    out='''ERROR: Invalid Marks 150 > 100'''
    res=run(main,inp)
    assert(res==out)