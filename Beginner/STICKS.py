# https://www.codechef.com/problems/STICKS

for T in range(int(input())):
    i,a,k,c=int(input())-1,sorted(list(map(int,input().split()))),-1,0
    while(i>0):
        if(a[i]==a[i-1]): 
            k,c,i=k*a[i],c+1,i-2
            if(c==2): break
        else: i-=1 
    print(abs(k)) if(c==2) else print(-1)