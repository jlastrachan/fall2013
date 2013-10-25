import sys
import random
import numpy
import PS23mycode

numbit = (0, 1)
reps = range(3)

aa = [[[1,1]],
      [[1,1,0],[1,0,1],[1,1,1]],
      [[1,1,0,0],[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],
       [1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,1]]]

if __name__ == "__main__":
    for a in aa:
        k = len(a)
        k1 = k+1
        m = len(a[0])
        n = k+m
        q = range(k)
        random.shuffle(q)
        A = numpy.array(a)[q,]
        jr = range(n+1)
        for i1 in xrange(2**k):
            msg0 = [[random.choice(numbit) for i2 in xrange(k)] for i3 in reps]
            msg1 = numpy.array(msg0)
            omsg = ''.join([str(x) for x in msg1.reshape(-1)])
            msg2 = numpy.hstack((msg1,msg1.dot(A)%2))
            msg3 = msg2.copy()
            for i2 in reps:
                j = random.choice(jr)
                if j<n:
                    msg3[i2,j] = 1 - msg3[i2,j]
            msg = ''.join([str(x) for x in msg3.reshape(-1)])
            try:
                cmsg = PS23mycode.recover(A,msg)
            except:
                print '\nA='
                print A
                raise StandardError('recover(A,"%s"):  failed to run'%msg)
            if not type(cmsg)==type(''):
                print '\nA='
                print A
                raise StandardError('recover(A,"%s"):  not a string'%msg)
            if not cmsg==omsg:
                print '\nA='
                print A
                print msg2
                print msg3
                raise StandardError('recover(A,"%s")="%s", not %s'%(msg,cmsg,omsg))    
        sys.stdout.write('+')
    print " GREAT! NO ERRORS FOUND"
