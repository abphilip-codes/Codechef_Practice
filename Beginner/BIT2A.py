# https://www.codechef.com/problems/BIT2A

for T in range(int(input())):
    n,a,b=int(input()),list(map(int,input().split())),[]
    for z in a:
        c=0
        for y in a:
            if(y>z): c+=1 
        b.append(c)
    print(*b)