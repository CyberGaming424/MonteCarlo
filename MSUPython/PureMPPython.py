from math import sqrt
import math
import random as ran
import time
import multiprocessing as mp
import concurrent.futures

ran.seed(123)
startTime = time.time()

def inCircle(set):
    x = set[0]
    y = set[1]
    d = sqrt((x * x) + (y * y))
    return  d < 1.0

def createSet():
    x = ran.random()
    y = ran.random()
    return [x, y]


def calc(inCircleAmount, size):
    setSize = round(size)
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    inCircleAmount.value += inCircleCount
    

def main():
    setSize = 10000000
    individualSetSize = setSize/10
    totalInCircleCount = mp.Value('i', 0)
    processes = []
    for i in range(10):
        processes.append(mp.Process(target=calc, args=(totalInCircleCount,individualSetSize)))

    for i in range(len(processes)):
        processes[i].start()
    for i in range(len(processes)):
        processes[i].join()
    Accuracy = (4 * (totalInCircleCount.value/setSize)) - math.pi
    print("Accuracy: " + str(Accuracy))

if __name__ == '__main__':
    main()
    print(time.time() - startTime)
    

    
