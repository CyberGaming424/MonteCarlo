import numpy as np
from numba import njit, prange
from math import sqrt
import math
import random as ran
import cProfile
import multiprocessing as mp
import concurrent.futures
import timeit

#N = [10000, 100000, 1000000, 10000000, 1000000000, 100000000000]

N = [1000, 10000]

#Raw Python
def raw():

    estimation = []
    times = []
    
    for i in len(N):
        startTime = timeit.default_timer
        acc = 0
        for i in range(N(i)):
            numSet = [ran.random(), ran.random()]
            if(numSet[0]**2 + numSet[1]**2)< 1.0:
                acc += 1
        estimation.append(4 * (acc/N(i)))
        times.append(timeit.default_timer - startTime)

#Raw parllel python
def inCircle(set):
    x = set[0]
    y = set[1]
    d = sqrt((x * x) + (y * y))
    return  d < 1.0

def createSet():
    x = ran.random()
    y = ran.random()
    return [x, y]


def calc(inCircleAmount, seed, size):
    setSize = round(size)
    ran.seed(seed)
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    inCircleAmount.value += inCircleCount
    

def RawPPython():

    test = [ 10000, 100000, 1000000, 10000000]

    estimation = []
    times = []
    
    for setSize in range(len(test)):
        startTime = timeit.default_timer()
        individualSetSize = test[setSize]/10
        totalInCircleCount = mp.Value('i', 0)
        processes = []
        
        for i in range(10):
            processes.append(mp.Process(target=calc, args=(totalInCircleCount,ran.random,individualSetSize)))

        for i in range(len(processes)):
            processes[i].start()
        for i in range(len(processes)):
            processes[i].join()

        estimation.append(4 * (totalInCircleCount.value/test[setSize]))
        times.append(timeit.default_timer() - startTime)
    print(estimation)
    print(times)

if __name__ == '__main__':
    #RawPPython()
    RawPPython()

