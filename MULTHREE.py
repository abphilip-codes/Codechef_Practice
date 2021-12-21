# https://www.codechef.com/problems/MULTHREE

for T in range(int(input())):
    k,d0,d1 = map(int,input().split())
    t = d0+d1
    ans,k,s = t,k-2,(2*t)%10+(4*t)%10+(8*t)%10+(6*t)%10
    if(k>0): ans,k = ans+(t%10),k-1
    ans+=(k//4)*s
    k,p = k%4,2
    for z in range(k):
        ans+=(p*t)%10
        p=(p*2)%10
    print("YES") if((ans%3)==0) else print("NO")