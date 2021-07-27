# https://www.codechef.com/problems/TWONMS

for T in range(int(input())):
    a,b,n=map(int,input().split())
    print(max(a*(2**(n+1)),b*(2**n))//min(a*(2**(n+1)),b*(2**n))) if(n%2!=0) else print(max(a*(2**n),b*(2**n))//min(a*(2**n),b*(2**n)))