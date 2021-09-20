# https://www.codechef.com/problems/HDIVISR

n=int(input())
for z in range(10,0,-1):
    if(n%z==0): 
        print(z)
        break