# https://www.codechef.com/problems/ISITCAKE

for _ in range(int(input())):
    count=0
    for z in range(10):
        l=list(map(int,input().split()))
        for y in range(10):
            if(l[y]<=30): count+=1 
    print("yes") if(count>=60) else print("no")