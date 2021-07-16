from math import sqrt
import random as ran
import cProfile

ran.seed(123)



def inCircle(set):
    x = set[0]
    y = set[1]
    d = sqrt((x * x) + (y * y))
    return  d < 1.0

def createSet():
    x = ran.random()
    y = ran.random()
    return [x, y]

def main():
    setSize = 1000000
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    print(4 * (inCircleCount / setSize))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', "output.dat")

    import pstats
    from pstats import SortKey

    #with open("output_time.txt", "w") as f:
        #p = pstats.Stats("output.dat", stream=f)
        #p.sort_stats("time").print_stats()

    with open("output_calls.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("call").print_stats()