#!/usr/bin/python3
#calculate the classical diffusion on a ring
import random
random.seed()

#set ring size
nNode=21

#set coupling strength
g=1e-5

#set total evolution time
nTime=100

stepTime=int(1/g)
nStep=nTime*stepTime

#set the initial condition
A=[0+0j for i in range(nNode)]
A[int(nNode/2)]=1+0j

#do simulation
for iStep in range(nStep):
    #calculate the diffusion speed
    dA=[(0+1j)*(A[(i+1)%nNode]+A[(i-1)%nNode]-2*A[i]) for i in range(nNode)]
    #calculate the new P
    A=[A[i]+g*dA[i] for i in range(nNode)]

    if iStep%stepTime == 0:
        for i in range(nNode):
            print(abs(A[i])**2,end='\t')
        print()

