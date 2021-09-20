# https://www.codechef.com/problems/CNDLOVE

for T in range(int(input())):
    n,a=int(input()),list(map(int,input().split()))
    print("YES") if(a%2!=0) else print("NO")