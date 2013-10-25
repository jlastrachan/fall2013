import PS50mycode
import random, math
import numpy as np

ndtype = type(np.zeros(1))

if __name__ == '__main__':
    for i in xrange(20):
        T = random.choice(xrange(3,9))
        M = random.choice(xrange(1,5))
        t0 = random.random()*T*0.99+0.01
        r = random.random()+0.2
        MT = M*T
        w = 2*math.pi/T
        receiver = PS50mycode.Receiver(T,M)
        N = random.choice([20,30,40])
        bts = np.array([random.choice([0,1]) for i in xrange(N)])
        bits = np.hstack((np.zeros(2*MT+random.choice(xrange(T))),
                          bts.repeat(M*T), np.zeros(20)))
        y = r*bits*np.sin(w*(np.array(xrange(len(bits)))-t0))
        tau = receiver.tau(y)
        ii, eye = receiver.eye(y)
        MT3 = 3*MT
        assert type(ii)==ndtype, 'ii: not an ndarray'
        assert ii.shape==(MT3,), 'ii: wrong shape'
        for j in xrange(MT3):
            assert abs(ii[j]-j)<0.0001, 'ii: wrong values'
        assert type(eye)==ndtype, 'eye: not an ndarray'
        Ny = len(y)
        v = np.convolve(y*np.sin(np.linspace(-w*tau,w*(Ny-1-tau),
                                             Ny)),np.ones(MT))
        k = len(v)/MT3
        assert eye.shape==(MT3,k), 'eye: wrong shape'
        eyet = eye.transpose().reshape(-1)
        for j in xrange(MT3*k):
            assert abs(eyet[j]-v[j])<0.0001, 'eye: wrong values'
        
    print "GREAT! NO ERRORS FOUND"
