import numpy as np
import sys
import math, cmath, random

import PS60mycode


if __name__ == '__main__':
    import psaudio
    import matplotlib.pyplot as plt
    import PS42mycode

    narg = len(sys.argv)
    T = 16
    if narg > 1:
        T = eval(sys.argv[1])
    M = 4
    if narg > 2:
        M = eval(sys.argv[2])
    C = [-1,-1,4,1,1]
    if narg > 3:
        C = eval(sys.argv[3])
    if type(C)==type(0):
        channel = psaudio.AudioChannel(C)
    else:
        channel = PS42mycode.AbstractChannel(0.0,np.array(C),25,25)
    bs = "1010110011001110001110001111000011110000111110000011111000001111"
    if narg > 4:
        bs = sys.argv[4]
    bits = np.array([int(x) for x in '1'+bs+'1'])
    
    sender = PS60mycode.Sender(T,M)
    receiver = PS60mycode.Receiver(T,M)
    zz = np.zeros(50)
    x = sender.band(sender.modulate(np.hstack((zz,bits,zz))))
    y = receiver.band(channel.sendreceive(x))
    b = receiver.demodulate(y)
    bb = b[b.argmax()+1:][::-1]
    bbb = bb[bb.argmax()+1:][::-1]
    bbs = ''.join([str(i) for i in bbb])
    print bs
    print bbs
    (ii,eye) = receiver.eye(y)

    
    plt.figure(1)
    plt.subplot(211)
    plt.plot(ii,eye,'b',ii[[0,-1]],receiver.gamma*np.ones(2),'r',
             ii[receiver.q0+M*T].repeat(2),
             np.array([0,eye.reshape(-1).max()]),'r')
    plt.grid()
    plt.subplot(212)
    plt.plot(receiver.Vq0,'.',
             np.array([0,len(receiver.Vq0)]),receiver.gamma*np.ones(2),'r')
    plt.grid()

    plt.show()
