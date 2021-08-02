# https://www.codechef.com/problems/ELEVSTRS

for T in range(int(input())):
    n,v1,v2=map(int,input().split())
    print("Elevator") if((2/v2)<((2**(1/2))/v1)) else print("Stairs")