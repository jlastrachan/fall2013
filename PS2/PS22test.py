import sys
import numpy
import PS22mycode

ndtype = type(numpy.array([[1,1],[1,1]]))

if __name__ == "__main__":
    for k in xrange(1,30):
        try:
            A = PS22mycode.optimal(k)
        except:
            raise StandardError('optimal(%d):  failed to run'%k)
        if not type(A)==ndtype:
            raise StandardError('optimal(%d):  not a numpy array'%k)
        if not A.ndim==2:
            raise StandardError('optimal(%d):  not two dimensional'%k)
        if not A.shape[0]==k:
            raise StandardError('optimal(%d):  wrong number of rows'%k)
        m = A.shape[1]
        if (2**(m-1)-m+1 > k) or (2**m-m <= k):
            raise StandardError('optimal(%d):  wrong number of columns'%k)
        if not ((A==0)+(A==1)).all():
            raise StandardError('optimal(%d):  not a 0/1 array'%k)
        if not (A.sum(1)>1.5).all():
            raise StandardError('optimal(%d):  no SEC (simple row)'%k)
        for i in xrange(k):
            for j in xrange(i):
                if (A[i,]==A[j,]).all():
                    raise StandardError('optimal(%d):  no SEC (double row)'%k)
        sys.stdout.write('+')
    print " GREAT! NO ERRORS FOUND"
