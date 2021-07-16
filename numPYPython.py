import numpy as np

def inCircle(arrayNums):
    return  np.sqrt((arrayNums[0]**2) + (arrayNums[1]**2)) < 1.0

def createSet():
    return np.random.random(2)

def main():
    setSize = 1000000
    inCircleCount = 0
    for x in range(setSize):
        if inCircle(createSet()):
            inCircleCount += 1
    print(4 * (inCircleCount / setSize))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', "output4.dat")

    import pstats
    from pstats import SortKey

    #with open("output_time.txt", "w") as f:
        #p = pstats.Stats("output.dat", stream=f)
        #p.sort_stats("time").print_stats()

    with open("output_calls4.txt", "w") as f:
        p = pstats.Stats("output4.dat", stream=f)
        p.sort_stats("call").print_stats()