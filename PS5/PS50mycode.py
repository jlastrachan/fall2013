import sys
import math, cmath, random
import numpy as np


class Communicator():
    
    def __init__( self, T=8, M=1):
        self.T = T
        self.M = M

        

class Sender(Communicator):

    def modulate(self, bits):
        return np.array([bits[int(t/self.T/self.M)]*math.sin(2*math.pi*t/self.T) for t in range(len(bits)*self.T*self.M)])      
    

class Receiver(Communicator):

    def tau(self, y):
        a = sum([y[t]*math.cos(2*math.pi/self.T*t) for t in range(len(y))])
        b = sum([y[t]*math.sin(2*math.pi/self.T*t) for t in range(len(y))])

        alpha = a/(math.sqrt(a**2 + b**2))
        beta = b/(math.sqrt(a**2 + b**2))

        tau_helper = complex(beta, -alpha)
        return cmath.phase(tau_helper)*self.T/2/math.pi % self.T

    def eye(self, y):
        result = []
        for k in range(int((len(y)+self.M*self.T -1)/(3*self.M*self.T))):
            result.append([self.get_v(y, i + 3*self.M*self.T*k) for i in range(3*self.M*self.T)])
        result = np.array(result).T
        return (np.array(xrange(3*self.M*self.T)), result)


    def get_v(self, y,i):
        tau = self.tau(y)
        x = [y[t]*math.sin(2*math.pi/self.T*(t-tau)) for t in range(len(y))]
        return sum(x[i-self.M*self.T +1:i+1])

            

if __name__ == '__main__':
    import psaudio
    import matplotlib.pyplot as plt
    import PS42mycode

    T = 8
    if len(sys.argv)>1:
        T = int(sys.argv[1])
    M = 1
    if len(sys.argv)>2:
        M = int(sys.argv[2])
    C = [-1,-1,4,1,1]
    if len(sys.argv)>3:
        C = eval(sys.argv[3])
    if type(C)==type(0):
        channel = psaudio.AudioChannel(C)
    else:
        channel = PS42mycode.AbstractChannel(C[0],np.array(C[1]),5*M*T,25)

    bts = np.array([random.choice((0,1)) for i in xrange(500)])
    bits = np.hstack((np.zeros(20),bts,np.zeros(20)))
    sender = Sender(T,M)
    receiver = Receiver(T,M)
    x = sender.modulate(bits)
    y = channel.sendreceive(x)
    tau = receiver.tau(y)
    ii,eye = receiver.eye(y)
   
    t = np.array(xrange(len(y)))
    v = np.sin(sender.w*(t-tau))*y
    
    plt.figure(1)
    plt.subplot(211)
    plt.plot(t,v)
    plt.grid()
    plt.subplot(212)
    plt.plot(ii, eye)
    plt.grid()
    plt.show()
