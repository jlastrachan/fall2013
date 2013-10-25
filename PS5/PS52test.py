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
        assert type(tau)==type(0.0), 'tau: not a float'
        assert abs(t0-tau)<0.001, 'tau: incorrect value'
    print "GREAT! NO ERRORS FOUND"
