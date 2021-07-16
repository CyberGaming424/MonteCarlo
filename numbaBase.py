import numpy as np
from numba import njit

userSize = 1000000

@njit(cache=True)
def main():
    acc = 0
    for i in range(userSize):
        numSet = np.random.random(2)
        if(numSet[0]**2 + numSet[1]**2)< 1.0:
            acc += 1
    print(4 * (acc/userSize))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', "output3.dat")

    import pstats
    from pstats import SortKey

    #with open("output_time.txt", "w") as f:
        #p = pstats.Stats("output.dat", stream=f)
        #p.sort_stats("time").print_stats()

    with open("output_calls3.txt", "w") as f:
        p = pstats.Stats("output3.dat", stream=f)
        p.sort_stats("call").print_stats()