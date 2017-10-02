from __future__ import division
def ask2a(a,b,nmax=4):
    I=0.0    
    dx=(b-a)/nmax
    for i in range(0,nmax):
        I+=3*(a+(i+0.5)*dx)-2
    I*=dx
    print I


ask2a(0,1,4)
