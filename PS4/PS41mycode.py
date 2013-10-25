import sys
import numpy as np

def analyse(channel, T=50000, n=50, k=50):
    """
    (x,fx,R) = analyse(channel,T,n,k)
    inputs:
      channel: instance of a class with method senreceive
               (channel.sendreceive takes one-dimensional Numpy array,
               returns one-dimensional Numpy array at leastas long)
      T: int (T>n, T>k)
      n: int (n>0)
      k: int (k>0)
    outputs:
      x:  one-dimensional Numpy array of length n
      fx: one-dimensional Numpy array of length n (non-negative)
      R:  one-dimensional Numpy array of length k
    """
    output = channel.sendreceive(np.zeros(T))
    histo_values, bin_vals = np.histogram(output, bins=n)

    x = np.array([(bin_vals[i] + bin_vals[i+1])/2 for i in range(n)])
    scaling_factor = sum([histo_values[i]*(bin_vals[i+1]-bin_vals[i]) for i in range(n)])
    fx = np.array([histo_values[i]/scaling_factor for i in range(n)])

    R = np.array([1] + [np.var(output[:-m]+output[m:])/(2*np.var(output)) - 1 for m in range(1,k)])

    return x, fx, R


if __name__ == '__main__':
    import psaudio
    import matplotlib.pyplot as plt
    
    fs = 8000
    if len(sys.argv)>1:
        fs = int(sys.argv[1])
    T = 50000
    if len(sys.argv)>2:
        T = int(sys.argv[2])
    n = 100
    if len(sys.argv)>3:
        n = int(sys.argv[3])
    k = 100
    if len(sys.argv)>4:
        k = int(sys.argv[4])
    
    audio = psaudio.AudioChannel(fs)
    (x,fx,R) = analyse(audio,T,n,k)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(x,fx)
    plt.grid()
    plt.xlabel('Noise PDF')
    plt.subplot(212)
    plt.plot(R,'r.-')
    plt.grid()
    plt.xlabel('Noise auto-correlation')
    plt.show()

    
