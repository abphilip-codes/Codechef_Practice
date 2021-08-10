# https://www.codechef.com/problems/PRGIFT

for T in range(int(input())):
    n,k=map(int,input().split())
    a,c=list(map(int,input().split())),0
    for i in a:
        if(i%2==0): c+=1
        else: c=0
        if(c==k and k!=0): 
            print("YES")
            break
    else: print("NO")