import numpy as np
import time

startTime = time.time()
np.random.seed(123)

def inCircle(arrayNums):
    return  np.sqrt((arrayNums[0]**2) + (arrayNums[1]**2)) < 1.0

def createSet():
    return np.random.random(2)

def main():
    setSize = 10000000
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    Accuracy = (4 * (inCircleCount/setSize)) - np.pi
    print("Accuracy: " + str(Accuracy))

main()
print(time.time() - startTime)
