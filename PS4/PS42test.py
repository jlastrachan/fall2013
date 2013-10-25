import random
import numpy as np
import PS42mycode

ndtype = type(np.zeros(1))

if __name__ == '__main__':
    for i in xrange(5):
        sigma = 0.5+np.random.randn(1)**2
        nh = random.choice(xrange(1,20))
        lag = random.choice(xrange(1,20))
        pad = random.choice(xrange(1,20))
        h = np.random.randn(nh)
        a = PS42mycode.AbstractChannel(sigma,h,lag,pad)
        T = random.choice([10000,9999,20000])
        x = 1+np.random.randn(T)
        y = a.sendreceive(x)
        assert type(y)==ndtype, 'y: not ndarray'
        assert y.shape==(lag+pad+T+nh-1,), 'y: wrong shape'
        v = y-np.hstack((np.zeros(lag),np.convolve(h,x),np.zeros(pad)))
        mu = v.mean()
        print '\n-------\n%f~0'%mu
        assert abs(mu)<0.1, 'y: noise mean mismatch'
        va = v.var()
        print '%f~%f'%(va,sigma**2)
        assert abs(va-sigma**2)/va<0.1, 'y: noise variances mismatch'
        
    print "GREAT! NO ERRORS FOUND"
        
