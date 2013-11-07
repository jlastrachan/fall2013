import math, cmath, random
import numpy as np
import matplotlib.pyplot as plt

def get_ft(N):
	n = np.linspace(0,N,N)
	x = np.sinc(n/math.pi)/math.pi
	X = np.fft.fft(x, 2**20)
	return X

def get_approx_ft(N):
	n = np.linspace(0,N,N)
	hB = np.sinc(n/math.pi)/math.pi
	hD = np.sinc(n*0.1/math.pi)*.1/math.pi
	p = ((math.pi/0.1)*hB)*hD
	return np.fft.fft(p, 2**20)

print "N=10"
P = get_approx_ft(10)
n = np.linspace(0,2*math.pi,2**20)
absP = abs(P)
print max(absP)
print "diff", max(absP)-1

print "N=100"
P = get_approx_ft(100)
n = np.linspace(0,2*math.pi,2**20)
absP = abs(P)
print "diff", max(absP)-1
print "N=1000"
P = get_approx_ft(1000)
n = np.linspace(0,2*math.pi,2**20)
absP = abs(P)
print "diff", max(absP)-1
print "N=10000"
P = get_approx_ft(10000)
n = np.linspace(0,2*math.pi,2**20)
absP = abs(P)
print max(absP)
print "diff", max(absP) -1

