import numpy as np
import sys
import math, cmath, random

import PS60mycode

NFFT = 2**20
ff = np.linspace(0,1,NFFT)
def fft(y):
    Y = np.abs(np.fft.fft(y,2*NFFT)[:NFFT])
    return Y/Y.max()

if __name__ == '__main__':
    import psaudio
    import matplotlib.pyplot as plt
    import PS42mycode

    narg = len(sys.argv)
    T = 16
    if narg > 1:
        T = eval(sys.argv[1])
    M = 1
    if narg > 2:
        M = eval(sys.argv[2])
    C = [-1,-1,4,1,1]
    if narg > 3:
        C = eval(sys.argv[3])
    if type(C)==type(0):
        channel = psaudio.AudioChannel(C)
    else:
        channel = PS42mycode.AbstractChannel(0.0,np.array(C),25,25)
    
    sender = PS60mycode.Sender(T,M)
    bitval = (0,1)
    bits = np.array([random.choice(bitval) for i in xrange(500)])
    zz = np.zeros(50)
    x0 = sender.modulate(np.hstack((zz,bits,zz)))
    x1 = sender.band(x0)
    y0 = channel.sendreceive(x0)
    z0 = sender.band(y0)
    y1 = channel.sendreceive(x1)
    z1 = sender.band(y0)
    H = fft(sender.h)
    X0 = fft(x0)
    X1 = fft(x1)
    Y0 = fft(y0)
    Y1 = fft(y1)
    Z0 = fft(z0)
    Z1 = fft(z1)
    b = (ff<0.3)
    plt.figure(1)
    plt.subplot(321)
    plt.plot(ff[b],X0[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.subplot(322)
    plt.plot(ff[b],X1[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.subplot(323)
    plt.plot(ff[b],Y0[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.subplot(324)
    plt.plot(ff[b],Y1[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.subplot(325)
    plt.plot(ff[b],Z0[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.subplot(326)
    plt.plot(ff[b],Z1[b],'b',ff[b],H[b],'r')
    plt.grid()
    plt.show()
