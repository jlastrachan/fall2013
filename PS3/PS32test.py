import sys
import random
import numpy as np
import PS32mycode

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
KK = (2,3,4,5,6,7)
rr = (1,2,3,4,5)
TT = (1,2,4,10)
YY = (-0.125,.0,.125,.25,.375,.5,.625,.75,.875,1.,1.125)
ndtype = type(np.array([]))

if __name__ == "__main__":
    for N in xrange(1,20):
        K = random.choice(KK)
        r = random.choice(rr)
        T = random.choice(TT)
        W0 = [[random.choice(bits) for i in xrange(K)] for j in xrange(r)]
        Ws = '[%s]'%','.join(['[%s]'%','.join([str(x) for x in y]) for y in W0])
        W=np.array(W0)
        u = np.array([random.choice(bits) for i in xrange(T)])
        Wc = [list(x) for x in list(W)]
        uc = list(u)
        yc = np.array(crazy(Wc,uc))
        ycs = '[%s]'%(','.join([str(x) for x in yc]))
        try:
            decoder = PS32mycode.Viterbi(W)
        except:
            print 'W=%s'%Ws
            raise StandardError('decoder=Viterbi(W):  failed to run')
        try:
            (uu, Pmin, unique) = decoder.decode(yc)
        except:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
failed to run'%ycs)
        if not type(uu)==ndtype:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is not a numpy array'%ycs)
        if not uu.shape==(T,):
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is of a wrong shape'%ycs)
        uul = list(uu)
        for x in uul:
            if x not in bits:
                'W=%s'%Ws
                raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is not a 0/1 vector'%ycs)
        yy = np.array(crazy(Wc,list(uu)))
        uus = '[%s]'%(','.join([str(x) for x in uu]))
        if ((yc-yy)**2).sum()>0.00001:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
incorrect output %s'%(ycs,uus))
        sys.stdout.write('+')

    KK = (1,2,3,4,5,6)
    for N in xrange(1,20):
        K = random.choice(KK)
        r = random.choice(rr)
        T = random.choice(TT)
        W0 = [[random.choice(bits) for i in xrange(K)] for j in xrange(r)]
        Ws = '[%s]'%','.join(['[%s]'%','.join([str(x) for x in y]) for y in W0])
        W=np.array(W0)
        yc = np.array([random.choice(YY) for i in xrange(r*T)])
        ycs = '[%s]'%(','.join([str(x) for x in yc]))
        Wc = [list(x) for x in list(W)]
        try:
            decoder = PS32mycode.Viterbi(W)
        except:
            print 'W=%s'%Ws
            raise StandardError('decoder=Viterbi(W):  failed to run')
        try:
            (uu, Pmin, unique) = decoder.decode(yc)
        except:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
failed to run'%ycs)
        if not type(uu)==ndtype:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is not a numpy array'%ycs)
        if not uu.shape==(T,):
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is of a wrong shape'%ycs)
        uul = list(uu)
        for x in uul:
            if x not in bits:
                print 'W=%s'%Ws
                raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
u is not a 0/1 vector'%ycs)
        uus = '[%s]'%(','.join([str(x) for x in uu]))
        pm = float('inf')
        uopt = []
        uniq = False
        for x in xrange(2**T,2**(T+1)):
            uc = [int(s) for s in bin(x)[3:]]
            y = crazy(Wc,uc)
            #print r, T, yc.shape, len(y)
            p = float(((yc-np.array(y))**2).sum())
            uniq = uniq and (p!=pm)
            if p<pm:
                pm=p
                uopt=uc
                uniq = True           
        yy = np.array(crazy(Wc,list(uu)))
        pmest = float(((yc-yy)**2).sum())
        if abs(pmest-Pmin)>0.00001:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
incorrect Pmin value %f vs. %f'%(ycs,Pmin,pmest))
        if uniq!=unique:
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
incorrect unique flag %s vs. %s'%(ycs,str(unique),str(uniq)))
        if abs(pm-Pmin)>0.00001:
            uopts = '[%s]'%(','.join([str(x) for x in uopt]))
            print 'W=%s'%Ws
            raise StandardError('(u,Pmin,unique)=decoder.decode(%s): \
not optimal %f vs. %f at %s'%(ycs,Pmin,pm,uopts))


        
        sys.stdout.write('o')

        
    print " GREAT! NO ERRORS FOUND"
    
