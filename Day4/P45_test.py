import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P45_solution import main
from P45 import main

def testcase1():
    inp='''7'''
    out='''Number of moves: 127'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''8'''
    out='''Number of moves: 255'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''3'''
    out='''Number of moves: 7'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''10'''
    out='''Number of moves: 1023'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''4'''
    out='''Number of moves: 15'''
    res=run(main,inp)
    assert(res==out)
