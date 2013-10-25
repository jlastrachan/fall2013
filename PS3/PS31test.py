import sys
import random
import numpy as np
import PS31mycode

def crazy(W,u):
    Wr = [w[:] for w in W]
    for w in Wr:
        w.reverse()
    K = len(W[0])
    u0 = (K-1)*[0]
    u0.extend(u)
    return [sum([x*y for x,y in zip(w,u0[j:j+K])])%2 \
         for j in xrange(len(u)) for w in Wr]

bits = (0,1)
KK = (4,5,6,7)
rr = (1,2,3,4,5)
TT = range(1,10)

ndtype = type(np.array([]))

if __name__ == "__main__":
    for N in xrange(1,20):
        K = random.choice(KK)
        r = random.choice(rr)
        T = random.choice(TT)
        W=np.array([[random.choice(bits) for i in xrange(K)] for j in xrange(r)])
        u = np.array([random.choice(bits) for i in xrange(T)])
        Wc = [list(x) for x in list(W)]
        uc = list(u)
        yc = np.array(crazy(Wc,uc))
        try:
            y = PS31mycode.conv(W,u)
        except:
            print 'W='
            print W
            raise StandardError('conv(W,%s):  failed to run'%str(u))
        if not type(y)==ndtype:
            print 'W='
            print W
            raise StandardError('conv(W,%s):  not a numpy array'%str(u))
        if not y.shape==(r*T,):
            print 'W='
            print W
            raise StandardError('conv(W,%s):  wrong shape'%str(u))
        yl = list(y)
        for x in yl:
            if x not in bits:
                print 'W='
                print W
                raise StandardError('conv(W,%s): not a 0/1 vector'%str(u))
        if abs(y-yc).sum()>0.00001:
            print 'W='
            print W
            raise StandardError('conv(W,%s):  incorrect output'%str(u))
        sys.stdout.write('+')

    print " GREAT! NO ERRORS FOUND"
    
