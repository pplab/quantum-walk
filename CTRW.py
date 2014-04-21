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
#P=[random.random() for i in range(nNode)]
P=[0 for i in range(nNode)]
P[int(nNode/2)]=100

#do simulation
for iStep in range(nStep):
    #calculate the diffusion speed
    dP=[P[(i+1)%nNode]+P[(i-1)%nNode]-2*P[i] for i in range(nNode)]
    #calculate the new P
    P=[P[i]+g*dP[i] for i in range(nNode)]

    if iStep%int(stepTime) == 0:
        for i in range(nNode):
            print(P[i],end='\t')
        print()

