import numpy as np
from numba import njit, prange
import time

userSize = 10000000
startTime = time.time()
np.random.seed(123)

@njit(parallel=True)
def main():
    acc = 0
    for i in prange(userSize):
        numSet = np.random.random(2)
        if(numSet[0]**2 + numSet[1]**2)< 1.0:
            acc += 1
    return ((4 * (acc/userSize)) - np.pi)
    

print("Accuracy:", main())
print(time.time() - startTime)

