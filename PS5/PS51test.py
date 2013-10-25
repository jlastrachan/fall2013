import random
import math
import numpy as np
import PS50mycode

ndtype = type(np.zeros(1))

if __name__ == '__main__':
    for i in xrange(10):
        T = random.choice(xrange(3,9))
        M = random.choice(xrange(1,5))
        w = 2*math.pi/T
        sender = PS50mycode.Sender(T,M)
        N = random.choice([20,30,40])
        bits = np.array([random.choice([0,1]) for i in xrange(N)])
        x = sender.modulate(bits)
        assert type(x)==ndtype, 'modulation: not ndarray'
        MT = M*T
        assert x.shape==(N*MT,), 'modulation: wrong shape'
        for j in xrange(N*MT):
            assert abs(x[j]-bits[j/MT]*math.sin(w*j))<0.001, 'incorrect modulation'
    print "GREAT! NO ERRORS FOUND"
