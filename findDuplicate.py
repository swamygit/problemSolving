import random
import sys

#Solution1: TC O(n), SC O(1)
def findDuplicate1(inp):
    n = len(inp)
    l = []
    d = {}
    for num in inp:
        if (num not in d):
            d[num] = num
        else:
            l.append(num)
    return l

#Solution2: TC O(n), SC O(1)
def findDuplicate2(inp):
    res = []
    for i in range(len(inp)):
        index = abs(inp[i]) - 1
        if(inp[index] < 0):
           res.append(index+1)
        else:
            inp[index] *= -1
    return res

    
#Main
def main():
    n = int(sys.argv[1])
    
    inp = [0] * n
    for i in range(n):
        inp[i] = i+1
    inp[n-1] = n-1
    
    print("inp: ", inp)
    print(findDuplicate1(inp))
    print(findDuplicate2(inp))
    
if __name__ == '__main__':
    main()
