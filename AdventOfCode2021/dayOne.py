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
    increase = 0
    