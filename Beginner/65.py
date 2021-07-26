# https://www.codechef.com/problems/RECTSQ

def gcd(a,b):
    while(b): a,b=b,a%b
    return a
for T in range(int(input())):
    a,b=map(int,input().split())
    c=gcd(a,b)
    print(int((a*b)/(c*c)))