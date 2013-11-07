import sys
import math, cmath, random
import numpy as np


if __name__ == '__main__':
    import PS60mycode
    ndtype = type(np.zeros(1))
    TT = range(3,20)
    MM = range(1,10)
    CC = [PS60mycode.Sender,PS60mycode.Receiver]
    NFFT = 2**15
    ff = np.linspace(0,1,NFFT)
    for i in xrange(10):
        T = random.choice(TT)
        M = random.choice(MM)
        C = random.choice(CC)
        f0 = 2.0/T
        com = C(T,M)
        assert type(com.h) == ndtype, 'h not ndarray'
        assert com.h.ndim == 1, 'h not one-dimensional'
        assert len(com.h)<300, 'h is too long'
        assert np.abs(com.h.imag).sum()<0.0001, 'h is not real'
        H = np.abs(np.fft.fft(com.h,2*NFFT)[:NFFT])
        assert H.max()<1.15, '|H| is not bounded by 1.15'
        assert H[ff<f0-0.025].max()<0.075, '|H| not <0.075 in stopband'
        assert H[ff>f0+0.025].max()<0.075, '|H| not <0.075 in stopband'
        assert H[abs(ff-f0)<0.015].min()>0.85, '|H| not >0.85 in passband'
    print "GREAT! NO ERRORS FOUND" 
            
        
        
