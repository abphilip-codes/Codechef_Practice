# https://www.codechef.com/problems/POTATOES

def isPrime(s):
    for a in range(2,s):
        if(s%a==0): return False
    return True
for T in range(int(input())):
    l=list(map(int,input().split()))
    s=sum(l)+1 
    while(True):
        if(isPrime(s)): 
            print(s-sum(l))
            break
        s+=1