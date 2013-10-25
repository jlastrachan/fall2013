import sys
import random
import numpy
import PS21mycode

numbit = (0,1)
strbit = ("0","1")

if __name__ == "__main__":
    for N in xrange(1,20):
        k = int(1+10*random.random())
        m = int(1+10*random.random())
        n = k+m
        A = numpy.array([random.choice(numbit) for j in xrange(k*m)]).reshape(k,m)
        msg = ''.join([random.choice(strbit) for j in xrange(k*N)])
        try:
            cmsg = PS21mycode.linear(A,msg)
        except:
            print 'A='
            print A
            raise StandardError('linear(A,"%s"):  failed to run'%msg)
        if not type(cmsg)==type(''):
            print 'A='
            print A
            raise StandardError('linear(A,"%s"):  not a string'%msg)
        if not len(cmsg)==n*N:
            print 'A='
            print A
            raise StandardError('linear(A,"%s"):  wrong length'%msg)
        for x in msg:
            if x not in strbit:
                print 'A='
                print A
                raise StandardError('linear(A,"%s"): not a binary string'%msg)          
        v = numpy.array([int(x) for x in msg]).reshape(N,k)
        u = numpy.array([int(x) for x in cmsg]).reshape(N,n)
        if not (((u[...,:k].dot(A)+u[...,k:])%2)==0).all():
            print 'A='
            print A
            raise StandardError('linear(A,"%s"):  wrong parity bits'%msg)
        if not (u[...,:k]==v).all():
            print 'A='
            print A
            raise StandardError('linear(A,"%s"):  wrong message bits'%msg)
        sys.stdout.write('+')
    print " GREAT! NO ERRORS FOUND"
    
    
    



