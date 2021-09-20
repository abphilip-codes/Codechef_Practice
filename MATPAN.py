# https://www.codechef.com/problems/MATPAN

for T in range(int(input())):
    price=list(map(int,input().split()))
    string,s=input().upper(),0
    for z in range(65,91):
        if(chr(z) not in string): s+=price[z-65]
    print(s)