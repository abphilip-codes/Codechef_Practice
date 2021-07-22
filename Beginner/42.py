# https://www.codechef.com/problems/TWOVSTEN

for T in range(int(input())):
    x = int(input())
    if(x%10==0): print(0)
    elif(x%5==0): print(1)
    else: print(-1)