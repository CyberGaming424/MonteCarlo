import numpy as np
from numba import njit, prange


userSize = 1000000

@njit(cache=True, parallel=True)
def createPair():
    numSet = np.random.random(2)
    if(numSet[0]**2 + numSet[1]**2)< 1.0:
        return True
    else: 
        return False

@njit(cache=True, parallel=True)
def main():
    acc = 0
    for i in prange(userSize):
        if createPair():
            acc += 1
    print(4 * (acc/userSize))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', "output5.dat")

    import pstats
    from pstats import SortKey

    #with open("output_time.txt", "w") as f:
        #p = pstats.Stats("output.dat", stream=f)
        #p.sort_stats("time").print_stats()

    with open("output_calls5.txt", "w") as f:
        p = pstats.Stats("output5.dat", stream=f)
        p.sort_stats("call").print_stats()