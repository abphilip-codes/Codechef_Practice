# https://www.codechef.com/problems/PAJAPONG

for _ in range(int(input())):
    x,y,k=map(int,input().split())
    print("Chef") if(((x+y)//k)%2==0) else print("Paja")