from math import sqrt
import math
import random as ran
import cProfile
import multiprocessing as mp
import concurrent.futures


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
    

def main():
    setSize = 100000
    individualSetSize = setSize/10
    totalInCircleCount = mp.Value('i', 0)
    processes = []
    for i in range(10):
        processes.append(mp.Process(target=calc, args=(totalInCircleCount,ran.random,individualSetSize)))

    for i in range(len(processes)):
        processes[i].start()
    for i in range(len(processes)):
        processes[i].join()

    print(totalInCircleCount.value)
    print((4 * (totalInCircleCount.value/setSize)))
    
if __name__ == '__main__':
    import cProfile
    cProfile.run('main()', "output2.dat")

    import pstats
    from pstats import SortKey

    with open("output_time2.txt", "w") as f:
        p = pstats.Stats("output2.dat", stream=f)
        p.sort_stats("time").print_stats()

    with open("output_calls2.txt", "w") as f:
        p = pstats.Stats("output2.dat", stream=f)
        p.sort_stats("call").print_stats()