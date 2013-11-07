import sys
import math, cmath, random
import numpy as np


if __name__ == '__main__':
    import PS60mycode
    ndtype = type(np.zeros(1))
    TT = range(10,20)
    MM = range(5,10)
    hh = [[-1,-1,4,-1,-1],[1,-3,1,1],[1,0,-4,1,1,0,1]]
    bitval = (0,1)
    for i in xrange(10):
        T = random.choice(TT)
        M = random.choice(MM)
        k = random.choice(xrange(2,10))
        h = np.hstack((-np.ones(k),2*k,-np.ones(k)))
        sender = PS60mycode.Sender(T,M)
        receiver = PS60mycode.Receiver(T,M)
        bits = np.array([random.choice(bitval) for j in xrange(50)])
        pbits = np.hstack((np.zeros(33),1,bits,1,np.zeros(30)))
        x = sender.modulate(pbits)
        y = np.convolve(h,x)+0.01*np.random.randn(len(h)+len(x)-1)
        b = receiver.demodulate(y)
        assert type(b)==ndtype, 'demodulate output: not ndarray'
        assert b.ndim==1, 'demodulate output: not one-dimensional'
        assert (b**2==b).all(), 'demodulate output: not 0/1'
        bb = b[b.argmax()+1:][::-1]
        bbb = bb[bb.argmax()+1:][::-1]
        print ''.join([str(b) for b in bits])
        print ''.join([str(b) for b in bbb])
        print ''
	print len(bbb), len(bits)
	print bbb
	print bits
        assert len(bbb)==len(bits), 'demodulate output: wrong length'
        assert (bbb==bits).all(), 'incorrect demodulation'
    print "GREAT! NO ERRORS FOUND"
                             
