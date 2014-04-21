#!/usr/bin/python3
# This program is to simulate classical random walks on a line.
# All walkers start at position 0 and do a random choice to walk left (position - 1) or right (position + 1).
# Collect all the walkers' position at every time.
import random
random.seed()
# set walkers' number
nWalker=1000

# set total walking time
totalTime=2000

# set ring size
ringSize=100

# set initial condition: time=0; all walker are at position 0
position=[0 for i in range(nWalker)]
amount=[0 for i in range(ringSize)]
amount[0]=nWalker

# do simulation
for time in range(0,totalTime):
    for walker in range(0,nWalker):
        p=position[walker]
        amount[p]-=1 
        step=random.choice([-1,1])
        p+=step
        if(p<0):
            p+=ringSize
        if(p>=ringSize):
            p-=ringSize
        position[walker]=p
        #count the number of positions
        amount[p]+=1
    for p in range(0,ringSize):
        print(amount[p],end='\t')
    print()
