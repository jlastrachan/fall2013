import random
import numpy as np
import PS41mycode

ndtype = type(np.zeros(1))

class A():
    def __init__(self, m, h):
        self.m = m
        self.h = h
    def sendreceive(self, x):
        return self.m+np.convolve(h,np.random.randn(x.size+20))
    

if __name__ == '__main__':
    for i in xrange(5):
        m = np.random.randn(1)
        h = np.random.randn(20)
        a = A(m,h)
        T = random.choice([90000,99999,110000])
        n = random.choice(xrange(90,110))
        k = random.choice(xrange(5,15))
        (x,fx,R) = PS41mycode.analyse(a,T,n,k)
        assert type(x)==ndtype, 'x: not ndarray'
        assert type(fx)==ndtype, 'fx: not ndarray'
        assert type(R)==ndtype, 'R: not ndarray'
        assert x.shape==(n,), 'x: wrong shape'
        assert fx.shape==(n,), 'fx: wrong shape'
        assert R.shape==(k,), 'R: wrong shape'
        assert (fx>=0).all(), 'x: not non-negative'
        M0 = sum(fx)*(x[1]-x[0])
        assert abs(1.0-M0)<0.001, 'x,fx: not PDF samples'
        print '\n------\n%f~1.0'%M0
        M1 = sum(fx*x)*(x[1]-x[0])
        assert abs(M1-m)<0.1, 'x,fx: the expected value does not match'
        print '%f~%f'%(M1,m)
        M2 = sum(fx*(x**2))*(x[1]-x[0])
        v = (h**2).sum()
        assert abs(M2-m**2-v)<1, 'x,fx: variance does not match'
        print '%f~%f'%(M2,v+m**2)
        assert abs(R[0]-1.0)<0.1, 'R[0]: not close to 1.0'
        print '%f~1.0'%R[0]
        for i in xrange(1,k):
            Ri = (h[i:]*h[:-i]).sum()/v
            assert abs(R[i]-Ri)<0.1, 'R: does not match'
            print '%f~%f'%(Ri,R[i])
    print "GREAT! NO ERRORS FOUND"
        
        
        
        
        

        
        
    
    
    
