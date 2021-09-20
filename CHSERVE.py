# https://www.codechef.com/problems/CHSERVE

for _ in range(int(input())):
    p1,p2,k=map(int,input().split())
    print("CHEF") if(((p1+p2)//k)%2==0) else print("COOK")