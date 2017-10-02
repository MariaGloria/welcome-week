from __future__ import division
import numpy as np
def ask2a(a,b,nmax=20):
    I=0.0    
    dx=(b-a)/nmax
    for i in range(0,nmax):
        I+=np.sin*((a+(i+0.5)*3*dx)
    I*=dx
    print I

ask2(0,pi,20)

