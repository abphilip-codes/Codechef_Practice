# https://www.codechef.com/problems/FLOW018

for T in range(int(input())):
    ans=1
    for i in range(1,int(input())+1): ans*=i 
    print(ans)