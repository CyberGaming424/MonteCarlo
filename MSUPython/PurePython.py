import math 
import random as ran
import time

ran.seed(123)



def inCircle(set):
    x = set[0]
    y = set[1]
    d = math.sqrt((x * x) + (y * y))
    return  d < 1.0

def createSet():
    x = ran.random()
    y = ran.random()
    return [x, y]

def main():
    setSize = 10000000
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    print("Accuracy:",(4 * (inCircleCount / setSize)) - math.pi )
startTime = time.time()
main()
print(time.time() - startTime)
