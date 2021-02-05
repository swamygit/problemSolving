import random
import sys

#Solution1: TC O(n log n), SC O(1)
def anagramCheck1(s,t):
        if(len(s) != len(t)):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if(s==t):
            return True
        return False

#Solution1: TC O(n), SC O(1)
def anagramCheck2(s,t):
        if(len(s) != len(t)):
            return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i])- ord('a')] += 1
            counts[ord(t[i])- ord('a')] -= 1
        for i in counts:
            if( i != 0 ):
                return False
        return True
        
    

def getRandomString(n):
    res = ''
    for i in range(n):
        c = chr(ord('a') + random.randint(0,25))
        res += c
    return res
#Main
def main():
    n = int(sys.argv[1])
    #s1 = getRandomString(n)
    #s2 = getRandomString(n)
    s1 = "aabcc"
    s2 = "aabcd"
    print("s1 :" , s1)
    print("s2 :" , s2)
    print(anagramCheck1(s1,s2))
    print(anagramCheck2(s1,s2))

    
if __name__ == '__main__':
    main()
