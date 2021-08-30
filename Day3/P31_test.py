import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P31_solution import main
from P31 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''18
           80
           90
           54'''
    out='''ERROR: Invalid Marks 54 > 50'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''-18
           -80
           -90
           -54'''
    out='''ERROR: Invalid Marks -18 < 0'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''15
           102
           -90
           56'''
    out='''ERROR: Invalid Marks 102 > 100'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''15
          -102
          -90
          56'''
    out='''ERROR: Invalid Marks -102 < 0'''
    res=run(main,inp)
    assert(res==out)
    
def testcase5() -> None:
    inp='''17
           100
           100
           -50'''
    out='''ERROR: Invalid Marks -50 < 0'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''20
           100
           150
           0'''
    out='''ERROR: Invalid Marks 150 > 100'''
    res=run(main,inp)
    assert(res==out)




