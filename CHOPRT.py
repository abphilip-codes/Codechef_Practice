# https://www.codechef.com/problems/CHOPRT

for T in range(int(input())):
    a,b = map(int,input().split())
    if(a>b): print(">")
    if(a<b): print("<")
    if(a==b): print("=")