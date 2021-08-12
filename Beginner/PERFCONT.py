# https://www.codechef.com/problems/PERFCONT

for T in range(int(input())):
    n,P=map(int,input().split())
    a=list(map(int,input().split()))
    ten=two=0
    for i in range(n):
        if(a[i]>=P//2): two+=1
        if(a[i]<=P//10): ten+=1
    print("yes") if(ten==2 and two==1) else print("no")