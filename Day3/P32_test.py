import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P32_solution import main
from P32 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''The lyrics are not that bad!'''
    out='''The lyrics are good!'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''Food is bad? not at all.'''
    out='''Food is bad? not at all.'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''The song is good.'''
    out='''The song is good.'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''The song is not extremely good.'''
    out='''The song is not extremely good.'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''His position in society is bad, though he is not a good person.'''
    out='''His position in society is bad, though he is not a good person.'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''His mood is not at all bad.'''
    out='''His mood is good.'''
    res=run(main,inp)
    assert(res==out)

def testcase7() -> None:
    inp='''heynotatallbadatall'''
    out='''heygoodatall'''
    res=run(main,inp)
    assert(res==out)

def testcase8() -> None:
    inp='''heynotsobad'''
    out='''heygood'''
    res=run(main,inp)
    assert(res==out)
