import sys
import numpy

def conv(W,u):
    """
    y = conv(W,u)
    W: r-by-K 0/1 numpy array 0/1 (for convolution code )
    u: 0/1 numpy vector of length T (binary input to be encoded)
    y: 0/1 numpy vector of length T*r (convolutional encoding of u)
    """
    r = len(W)
    K = len(W[0])
    result = []
    
    for index in range(len(u)):
        if index < K-1:
            window = [0]*(K-index-1) + u.tolist()[:index+1]
            window = numpy.array(window)
        else:
            window = u.tolist()[index-K+1: index+1]
        for i in range(r):
            p = sum(numpy.convolve(W[i], window, 'valid'))
            p %= 2
            result.append(p)
    return numpy.array(result)


    

if __name__ == "__main__":
    if len(sys.argv)>2:
        W = numpy.array(eval(sys.argv[1]))
        u = numpy.array([int(x) for x in sys.argv[2]])
        print ''.join([str(int(x)) for x in conv(W,u)])
    
    
