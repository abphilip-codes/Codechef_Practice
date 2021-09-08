# https://www.codechef.com/problems/COVIDLQ

for _ in range(int(input())):
    n,l,last=int(input()),list(map(int,input().split())),-6
    for z in range(len(l)):
        if(l[z]==1): 
            if((z-last)<6): 
                print("NO")
                break
            else: last=z
    else: print("YES")