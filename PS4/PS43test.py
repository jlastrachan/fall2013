import random
import math
import numpy as np
import PS43mycode

ndtype = type(np.zeros(1))

class A():
    def sendreceive(self, x):
        return x

if __name__ == '__main__':
    for i in xrange(5):
        print '*'
        T = random.choice(xrange(3,9))
        w = 2*math.pi/T
        a = A()
        bbch = PS43mycode.BasebandChannel(a,T)
        N = random.choice([20,30,40])
        bits = np.array([random.choice([0,1]) for i in xrange(N)])
        x = bbch.modulate(bits)
        assert type(x)==ndtype, 'modulation: not ndarray'
        assert x.shape==(N*T,), 'modulation: wrong shape'
        for i in xrange(N*T):
            assert abs(x[i]-bits[i/T]*math.sin(w*i))<0.001, 'incorrect modulation'
        e = bbch.demodulate(x)
        assert type(e)==ndtype, 'demodulation: not ndarray'
        assert e.shape==(N,), 'demodulation: wrong shape'
        assert (abs(2*e-bits)<0.0001).all(), 'incorrect demodulation'
    print "GREAT! NO ERRORS FOUND"
