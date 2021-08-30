import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P44_solution import main
from P44 import main

def testcase1() -> None:
    inp='''10'''
    out='''1'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''5624434677'''
    out='''3'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''23451'''
    out='''6'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''987651234'''
    out='''9'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''45632'''
    out='''2'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''34567'''
    out='''7'''
    res=run(main,inp)
    assert(res==out)