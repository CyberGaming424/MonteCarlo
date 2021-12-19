# Part One
'''with open('AdventOfCode2021/dayOne.txt') as dayOne:
    lines  = dayOne.readlines()
    increases = 0
    previous = 0
    for x in lines:
        if(previous != 0):
            if(int(x) > previous):
                increases += 1
        previous = int(x)
    print(increases)
    dayOne.close'''

# Part Two
with open('AdventOfCode2021/dayOne.txt') as dayOne:
    lines  = dayOne.readlines()
    increased = 0
    previousSum = 0
    for x in range(len(lines)):
        if(x < (len(lines)-2)):
            currentSum = int(lines[x])+int(lines[x+1])+int(lines[x+2])
            if(previousSum != 0):
                if(currentSum > previousSum):
                    increased += 1
            previousSum = currentSum
    print(increased)
    dayOne.close
        

