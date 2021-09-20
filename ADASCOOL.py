# https://www.codechef.com/problems/ADASCOOL

for T in range(int(input())):
    a,b=map(int,input().split())
    print("YES") if(a%2==0 or b%2==0) else print("NO")