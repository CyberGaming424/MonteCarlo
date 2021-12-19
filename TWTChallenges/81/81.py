def shouldSwap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1

permutations = []
def findPermutations(string, index, n):
    if index >= n:
        permutations.append(''.join(string))
        return
    for i in range(index, n):
        check = shouldSwap(string, index, i)
        if check:
            string[index], string[i] = string[i], string[index]
            findPermutations(string, index + 1, n)
            string[index], string[i] = string[i], string[index]
 
# Driver code
if __name__ == "__main__":
 
    string = list("223")
    n = len(string)
    for x in range(n+1):
        s = []
        for y in range(x):
          s.append(string[y])
        print(s)
        findPermutations(''.join(s), 0, len(s))
    print(permutations)