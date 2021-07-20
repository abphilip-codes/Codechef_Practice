# https://www.codechef.com/problems/FLOW016

for T in range(int(input())):
    a,b = map(int,input().split())
    c=a*b
    while(b): a,b = b,a%b
    print(a,c//a)