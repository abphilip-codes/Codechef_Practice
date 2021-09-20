# https://www.codechef.com/problems/PRGIFT

for T in range(int(input())):
    n,k=map(int,input().split())
    a,c=list(map(int,input().split())),0
    if(k in range(1,n+1)):
        for i in a:
            if(i%2==0): c+=1
            else: c=0
            if(c==k): 
                print("YES")
                break
        else: 
            print("YES") if(c==k) else print("NO")
    else: print("NO")