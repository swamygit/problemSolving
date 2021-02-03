import random
import sys

#Solution1: TC O(n2), SC O(1)
def rotateArray1(inp,k):
    n = len(inp)
    for i in range(k):
        last = inp[n-1]
        for j in range(n-2, -1, -1):
            inp[j+1] = inp[j]
        inp[0] = last
    return inp
    
    
#Solution2: TC O(n), SC O(n)
def rotateArray2(inp, k):
    n  = len(inp)
    res = [0] * n
    for i in range(n):
        res[(i+k)%n] = inp[i]
    return res
    
#Solution3: TC O(n), SC O(1)
def swap(inp, l, r):
    temp = inp[l]
    inp[l] = inp[r]
    inp[r] = temp
def reverse(inp, l, r):
    while l<r:
        swap(inp, l, r)
        l += 1
        r -= 1
def rotateArray3(inp, k):
    n = len(inp)
    reverse(inp, 0, n-1)
    reverse(inp, 0, k-1)
    reverse(inp, k, n-1)
    
    return inp
    
#Main
def main():
    n = int(sys.argv[1])
    k=2
    inp = []
    for i in range(n):
        inp.append(i)
    
    print("inp: ", inp, "\n","k= ", k)
    #print(rotateArray1(inp,k))
    print(rotateArray2(inp,k))
    #print(rotateArray3(inp,k))
    #print("output: ", inp)
    
if __name__ == '__main__':
    main()
