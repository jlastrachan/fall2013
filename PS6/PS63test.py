import sys
import math, cmath, random
import numpy as np


if __name__ == '__main__':
    import PS60mycode
    ndtype = type(np.zeros(1))
    TT = range(10,20)
    MM = range(5,10)
    bitval = (0,1)
    bark = np.array([0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0])
    for i in xrange(10):
        T = random.choice(TT)
        M = random.choice(MM)
        k1 = random.choice(xrange(2,40))
        k2 = random.choice(xrange(2,40))
        receiver = PS60mycode.Receiver(T,M)
        b1 = np.array([random.choice(bitval) for j in xrange(k1)])
        b1[::4] = 1
        b2 = np.array([random.choice(bitval) for j in xrange(k2)])
        b2[::4] = 1
        bits = np.hstack((b1,1,bark,b2))
        pos = receiver.preamble(bits)
        assert pos==(k1+1)
    print "GREAT! NO ERRORS FOUND"
